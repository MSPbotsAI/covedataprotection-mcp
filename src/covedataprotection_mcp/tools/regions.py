import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_region(region_info: dict) -> str:
        """Cove Data Protection Management Service method: AddRegion.

        JSON-RPC method: AddRegion

        Args:
            region_info: Required. Maps to "regionInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"regionInfo": region_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddRegion", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_regions() -> str:
        """Cove Data Protection Management Service method: EnumerateRegions.

        JSON-RPC method: EnumerateRegions

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateRegions", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
