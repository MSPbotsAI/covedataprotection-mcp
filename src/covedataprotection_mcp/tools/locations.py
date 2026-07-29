import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_location(location_info: dict) -> str:
        """Cove Data Protection Management Service method: AddLocation.

        JSON-RPC method: AddLocation

        Args:
            location_info: Required. Maps to "locationInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"locationInfo": location_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddLocation", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_locations() -> str:
        """Cove Data Protection Management Service method: EnumerateLocations.

        JSON-RPC method: EnumerateLocations

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateLocations", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_location_info(location_id: int) -> str:
        """Cove Data Protection Management Service method: GetLocationInfo.

        JSON-RPC method: GetLocationInfo

        Args:
            location_id: Required. Maps to "locationId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"locationId": location_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetLocationInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_location_info_by_name(location_name: str) -> str:
        """Cove Data Protection Management Service method: GetLocationInfoByName.

        JSON-RPC method: GetLocationInfoByName

        Args:
            location_name: Required. Maps to "locationName" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"locationName": location_name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetLocationInfoByName", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_return_account_to_home_location(account_id: int) -> str:
        """Cove Data Protection Management Service method: ReturnAccountToHomeLocation.

        JSON-RPC method: ReturnAccountToHomeLocation

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ReturnAccountToHomeLocation", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
