import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:
    @mcp.tool()
    async def covedataprotection_add_account(account_info: dict, home_node_info: dict) -> str:
        """Cove Data Protection Management Service method: AddAccount.

        JSON-RPC method: AddAccount

        Args:
            account_info: Required. Maps to "accountInfo" (dict).
            home_node_info: Required. Maps to "homeNodeInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountInfo": account_info, "homeNodeInfo": home_node_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddAccount", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_statistics(query: dict) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountStatistics.

        JSON-RPC method: EnumerateAccountStatistics

        Args:
            query: Required. Maps to "query" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"query": query}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountStatistics", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_accounts(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateAccounts.

        JSON-RPC method: EnumerateAccounts

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccounts", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_features(account_id: int) -> str:
        """Cove Data Protection Management Service method: GetAccountFeatures.

        JSON-RPC method: GetAccountFeatures

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountFeatures", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_info(name: str, password: str) -> str:
        """Cove Data Protection Management Service method: GetAccountInfo.

        JSON-RPC method: GetAccountInfo

        Args:
            name: Required. Maps to "name" (str).
            password: Required. Maps to "password" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"name": name, "password": password}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_info_by_id(account_id: int) -> str:
        """Cove Data Protection Management Service method: GetAccountInfoById.

        JSON-RPC method: GetAccountInfoById

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountInfoById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_account(account_info: dict, force_remove_custom_column_values_in_old_scope: bool) -> str:
        """Cove Data Protection Management Service method: ModifyAccount.

        JSON-RPC method: ModifyAccount

        Args:
            account_info: Required. Maps to "accountInfo" (dict).
            force_remove_custom_column_values_in_old_scope: Required. Maps to "forceRemoveCustomColumnValuesInOldScope" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountInfo": account_info, "forceRemoveCustomColumnValuesInOldScope": force_remove_custom_column_values_in_old_scope}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyAccount", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_account(account_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveAccount.

        JSON-RPC method: RemoveAccount

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveAccount", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_account_features(account_id: int, features: dict) -> str:
        """Cove Data Protection Management Service method: SetAccountFeatures.

        JSON-RPC method: SetAccountFeatures

        Args:
            account_id: Required. Maps to "accountId" (int).
            features: Required. Maps to "features" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id, "features": features}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetAccountFeatures", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
