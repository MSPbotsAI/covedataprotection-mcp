import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_get_amazon_endpoint_for_email(email: str) -> str:
        """Cove Data Protection Management Service method: GetAmazonEndpointForEmail.

        JSON-RPC method: GetAmazonEndpointForEmail

        Args:
            email: Required. Maps to "email" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"email": email}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAmazonEndpointForEmail", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_register_email(email: str) -> str:
        """Cove Data Protection Management Service method: RegisterEmail.

        JSON-RPC method: RegisterEmail

        Args:
            email: Required. Maps to "email" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"email": email}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RegisterEmail", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_unregister_email(email: str) -> str:
        """Cove Data Protection Management Service method: UnregisterEmail.

        JSON-RPC method: UnregisterEmail

        Args:
            email: Required. Maps to "email" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"email": email}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UnregisterEmail", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
