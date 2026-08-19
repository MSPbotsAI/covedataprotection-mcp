from collections.abc import Callable

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from .._json import dump_json_capped
from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:
    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True, idempotentHint=True))
    async def covedataprotection_get_server_info() -> str:
        """Get the Cove Management Service server version/info. Useful as a connectivity check."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        try:
            result = await client.call("GetServerInfo", {})
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()
