import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_enumerate_templates(partner_id: int, partner_only: bool) -> str:
        """Cove Data Protection Management Service method: EnumerateTemplates.

        JSON-RPC method: EnumerateTemplates

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            partner_only: Required. Maps to "partnerOnly" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "partnerOnly": partner_only}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateTemplates", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
