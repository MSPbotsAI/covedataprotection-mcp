from typing import Any

import httpx


class CoveError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(f"Cove Data Protection API error {status_code}: {message}")


class CoveClient:
    """Async httpx client wrapping the Cove Data Protection (N-able Backup
    Manager) JSON-RPC Management Service API.

    Unlike a static API key, this API requires an explicit Login exchange
    (partner/username/password) that returns a short-lived "visa" session
    token (valid ~15 minutes). Rather than caching a visa across requests —
    which would mean persisting session state — this client logs in fresh
    on every call() and discards the visa afterward, trading one extra HTTP
    round trip per call for full statelessness.
    """

    def __init__(self, partner: str, username: str, password: str, base_url: str):
        self._partner = partner
        self._username = username
        self._password = password
        self._base_url = base_url

    async def call(self, method: str, params: dict | None = None) -> Any:
        async with httpx.AsyncClient(timeout=30.0) as client:
            visa = await self._login(client)
            return await self._invoke(client, method, params, visa)

    async def _login(self, client: httpx.AsyncClient) -> str:
        body = {
            "jsonrpc": "2.0",
            "id": "login",
            "method": "Login",
            "params": {
                "partner": self._partner,
                "username": self._username,
                "password": self._password,
            },
        }
        data = await self._post(client, body)
        visa = data.get("visa")
        if not visa:
            raise CoveError(401, "Login succeeded but no visa was returned")
        return visa

    async def _invoke(
        self, client: httpx.AsyncClient, method: str, params: dict | None, visa: str
    ) -> Any:
        body = {
            "jsonrpc": "2.0",
            "visa": visa,
            "id": "jsonrpc",
            "method": method,
            "params": params or {},
        }
        data = await self._post(client, body)
        return data.get("result")

    async def _post(self, client: httpx.AsyncClient, body: dict) -> dict:
        try:
            resp = await client.post(self._base_url, json=body)
        except httpx.RequestError as e:
            raise CoveError(0, f"{e or type(e).__name__} (url={self._base_url})") from e
        data = self._parse_body(resp)
        self._raise_for_error(resp, data)
        return data

    def _parse_body(self, resp: httpx.Response) -> dict:
        if not resp.content:
            return {}
        try:
            parsed = resp.json()
            return parsed if isinstance(parsed, dict) else {"raw_response": parsed}
        except ValueError:
            return {"raw_response": resp.text}

    def _raise_for_error(self, resp: httpx.Response, data: dict) -> None:
        if "error" in data:
            err = data["error"]
            if isinstance(err, dict):
                msg = err.get("message") or err.get("code") or str(err)
            else:
                msg = str(err)
            raise CoveError(resp.status_code, msg)
        if resp.status_code >= 400:
            raise CoveError(resp.status_code, data.get("raw_response") or resp.text)
