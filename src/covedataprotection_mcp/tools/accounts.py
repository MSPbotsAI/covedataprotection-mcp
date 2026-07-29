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
    async def covedataprotection_add_account_node(account_node_info: dict) -> str:
        """Cove Data Protection Management Service method: AddAccountNode.

        JSON-RPC method: AddAccountNode

        Args:
            account_node_info: Required. Maps to "accountNodeInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountNodeInfo": account_node_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddAccountNode", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_add_account_profile(account_profile_info: dict) -> str:
        """Cove Data Protection Management Service method: AddAccountProfile.

        JSON-RPC method: AddAccountProfile

        Args:
            account_profile_info: Required. Maps to "accountProfileInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountProfileInfo": account_profile_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddAccountProfile", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_nodes_by_account_token(token: str) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountNodesByAccountToken.

        JSON-RPC method: EnumerateAccountNodesByAccountToken

        Args:
            token: Required. Maps to "token" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"token": token}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountNodesByAccountToken", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_profiles(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountProfiles.

        JSON-RPC method: EnumerateAccountProfiles

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountProfiles", params)
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
    async def covedataprotection_enumerate_ever_hosted_accounts(storage_node_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateEverHostedAccounts.

        JSON-RPC method: EnumerateEverHostedAccounts

        Args:
            storage_node_id: Required. Maps to "storageNodeId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeId": storage_node_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateEverHostedAccounts", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_removed_accounts_by_ids(account_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateRemovedAccountsByIds.

        JSON-RPC method: EnumerateRemovedAccountsByIds

        Args:
            account_ids: Required. Maps to "accountIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountIds": account_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateRemovedAccountsByIds", params)
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
    async def covedataprotection_get_account_id(account_name: str, account_password: str) -> str:
        """Cove Data Protection Management Service method: GetAccountId.

        JSON-RPC method: GetAccountId

        Args:
            account_name: Required. Maps to "accountName" (str).
            account_password: Required. Maps to "accountPassword" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountName": account_name, "accountPassword": account_password}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountId", params)
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
    async def covedataprotection_get_account_info_by_id_with_removed(account_id: int) -> str:
        """Cove Data Protection Management Service method: GetAccountInfoByIdWithRemoved.

        JSON-RPC method: GetAccountInfoByIdWithRemoved

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountInfoByIdWithRemoved", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_info_by_token(token: str) -> str:
        """Cove Data Protection Management Service method: GetAccountInfoByToken.

        JSON-RPC method: GetAccountInfoByToken

        Args:
            token: Required. Maps to "token" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"token": token}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountInfoByToken", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_node_info(account_node_id: int) -> str:
        """Cove Data Protection Management Service method: GetAccountNodeInfo.

        JSON-RPC method: GetAccountNodeInfo

        Args:
            account_node_id: Required. Maps to "accountNodeId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountNodeId": account_node_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountNodeInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_node_info_by_guid(node_guid: str) -> str:
        """Cove Data Protection Management Service method: GetAccountNodeInfoByGuid.

        JSON-RPC method: GetAccountNodeInfoByGuid

        Args:
            node_guid: Required. Maps to "nodeGuid" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"nodeGuid": node_guid}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountNodeInfoByGuid", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_account_profile_info(account_profile_id: int) -> str:
        """Cove Data Protection Management Service method: GetAccountProfileInfo.

        JSON-RPC method: GetAccountProfileInfo

        Args:
            account_profile_id: Required. Maps to "accountProfileId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountProfileId": account_profile_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAccountProfileInfo", params)
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
    async def covedataprotection_modify_account_profile(account_profile_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyAccountProfile.

        JSON-RPC method: ModifyAccountProfile

        Args:
            account_profile_info: Required. Maps to "accountProfileInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountProfileInfo": account_profile_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyAccountProfile", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_accounts_batch(account_ids: list[int], account_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyAccountsBatch.

        JSON-RPC method: ModifyAccountsBatch

        Args:
            account_ids: Required. Maps to "accountIds" (list[int]).
            account_info: Required. Maps to "accountInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountIds": account_ids, "accountInfo": account_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyAccountsBatch", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_relocate_account_node_by_token(token: str, from_storage_node_id: int, to_storage_node_id: int) -> str:
        """Cove Data Protection Management Service method: RelocateAccountNodeByToken.

        JSON-RPC method: RelocateAccountNodeByToken

        Args:
            token: Required. Maps to "token" (str).
            from_storage_node_id: Required. Maps to "fromStorageNodeId" (int).
            to_storage_node_id: Required. Maps to "toStorageNodeId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"token": token, "fromStorageNodeId": from_storage_node_id, "toStorageNodeId": to_storage_node_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RelocateAccountNodeByToken", params)
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
    async def covedataprotection_remove_account_data(account_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveAccountData.

        JSON-RPC method: RemoveAccountData

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveAccountData", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_account_profile(account_profile_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveAccountProfile.

        JSON-RPC method: RemoveAccountProfile

        Args:
            account_profile_id: Required. Maps to "accountProfileId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountProfileId": account_profile_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveAccountProfile", params)
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
