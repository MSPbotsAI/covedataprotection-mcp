import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_custom_column(custom_column: dict) -> str:
        """Cove Data Protection Management Service method: AddCustomColumn.

        JSON-RPC method: AddCustomColumn

        Args:
            custom_column: Required. Maps to "customColumn" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"customColumn": custom_column}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddCustomColumn", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_columns(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateColumns.

        JSON-RPC method: EnumerateColumns

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateColumns", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_custom_columns(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateCustomColumns.

        JSON-RPC method: EnumerateCustomColumns

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateCustomColumns", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_custom_column_values(account_id: int) -> str:
        """Cove Data Protection Management Service method: GetAccountCustomColumnValues.

        JSON-RPC method: GetAccountCustomColumnValues

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountCustomColumnValues", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_custom_column_info_by_id(custom_column_id: int) -> str:
        """Cove Data Protection Management Service method: GetCustomColumnInfoById.

        JSON-RPC method: GetCustomColumnInfoById

        Args:
            custom_column_id: Required. Maps to "customColumnId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"customColumnId": custom_column_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetCustomColumnInfoById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_custom_column(custom_column: dict) -> str:
        """Cove Data Protection Management Service method: ModifyCustomColumn.

        JSON-RPC method: ModifyCustomColumn

        Args:
            custom_column: Required. Maps to "customColumn" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"customColumn": custom_column}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyCustomColumn", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_custom_column(custom_column_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveCustomColumn.

        JSON-RPC method: RemoveCustomColumn

        Args:
            custom_column_id: Required. Maps to "customColumnId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"customColumnId": custom_column_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveCustomColumn", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_update_account_custom_column_values(account_id: int, values: dict) -> str:
        """Cove Data Protection Management Service method: UpdateAccountCustomColumnValues.

        JSON-RPC method: UpdateAccountCustomColumnValues

        Args:
            account_id: Required. Maps to "accountId" (int).
            values: Required. Maps to "values" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id, "values": values}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UpdateAccountCustomColumnValues", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
