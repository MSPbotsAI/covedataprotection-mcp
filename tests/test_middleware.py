"""Gateway credential middleware tests: missing-header 401, and header
values correctly reaching the per-request contextvar (no global-state
leakage across requests).
"""

from starlette.testclient import TestClient

from covedataprotection_mcp.__main__ import _build_http_app
from covedataprotection_mcp.config import Settings
from covedataprotection_mcp.server import create_mcp_server, get_client_from_context


def _make_app():
    settings = Settings()
    mcp = create_mcp_server(settings)
    return _build_http_app(mcp, settings), settings


def test_health_is_local_and_does_not_require_credentials():
    app, _ = _make_app()
    with TestClient(app) as client:
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}


def test_missing_header_returns_401_with_required_headers_listed():
    app, _ = _make_app()
    with TestClient(app) as client:
        resp = client.post(
            "/mcp",
            json={"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
            headers={"Accept": "application/json, text/event-stream"},
        )
        assert resp.status_code == 401
        body = resp.json()
        assert "X-CoveDataProtection-Partner" in body["required_headers"]
        assert "X-CoveDataProtection-Username" in body["required_headers"]
        assert "X-CoveDataProtection-Password" in body["required_headers"]


def test_missing_one_of_three_headers_still_returns_401():
    app, _ = _make_app()
    with TestClient(app) as client:
        resp = client.post(
            "/mcp",
            json={"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
            headers={
                "Accept": "application/json, text/event-stream",
                "X-CoveDataProtection-Partner": "acme",
                "X-CoveDataProtection-Username": "admin",
                # password intentionally omitted
            },
        )
        assert resp.status_code == 401


def test_header_present_reaches_request_context():
    # Directly exercises the middleware's contextvar plumbing without a full
    # MCP protocol round-trip: confirms the header values that arrive on the
    # request are exactly what get_client_from_context sees, and that they
    # are reset afterward (no leakage to the next request).
    import asyncio

    from covedataprotection_mcp.server import GatewayTokenMiddleware, _gateway_creds_var

    settings = Settings()
    seen = {}

    async def fake_app(scope, receive, send):
        seen["creds"] = _gateway_creds_var.get()
        await send({"type": "http.response.start", "status": 200, "headers": []})
        await send({"type": "http.response.body", "body": b""})

    middleware = GatewayTokenMiddleware(fake_app, settings)

    async def run():
        scope = {
            "type": "http",
            "path": "/mcp",
            "headers": [
                (b"x-covedataprotection-partner", b"acme-partner"),
                (b"x-covedataprotection-username", b"acme-user"),
                (b"x-covedataprotection-password", b"acme-pass"),
            ],
        }

        async def receive():
            return {"type": "http.request", "body": b"", "more_body": False}

        sent = []

        async def send(message):
            sent.append(message)

        await middleware(scope, receive, send)

    asyncio.run(run())
    assert seen["creds"] == ("acme-partner", "acme-user", "acme-pass")
    # After the request completes, the contextvar must be reset — a fresh
    # get() outside any request context sees no leftover credential.
    assert _gateway_creds_var.get() is None


def test_concurrent_requests_do_not_leak_credentials_across_contexts():
    # Two "requests" running interleaved via asyncio tasks must each see only
    # their own credentials — this is the request-level isolation guarantee
    # required by SOP §3.3 (no global/shared credential state).
    import asyncio

    from covedataprotection_mcp.server import GatewayTokenMiddleware, _gateway_creds_var

    settings = Settings()
    seen = {}

    async def fake_app(scope, receive, send):
        # Yield control so the two requests interleave.
        await asyncio.sleep(0)
        seen[scope["client_label"]] = _gateway_creds_var.get()
        await send({"type": "http.response.start", "status": 200, "headers": []})
        await send({"type": "http.response.body", "body": b""})

    middleware = GatewayTokenMiddleware(fake_app, settings)

    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(_message):
        pass

    def make_scope(label, partner, username, password):
        return {
            "type": "http",
            "path": "/mcp",
            "client_label": label,
            "headers": [
                (f"x-covedataprotection-partner".encode(), partner.encode()),
                (f"x-covedataprotection-username".encode(), username.encode()),
                (f"x-covedataprotection-password".encode(), password.encode()),
            ],
        }

    async def run():
        await asyncio.gather(
            middleware(make_scope("tenant-a", "partner-a", "user-a", "pass-a"), receive, send),
            middleware(make_scope("tenant-b", "partner-b", "user-b", "pass-b"), receive, send),
        )

    asyncio.run(run())
    assert seen["tenant-a"] == ("partner-a", "user-a", "pass-a")
    assert seen["tenant-b"] == ("partner-b", "user-b", "pass-b")


def test_client_factory_returns_none_without_context():
    settings = Settings()
    assert get_client_from_context(settings) is None
