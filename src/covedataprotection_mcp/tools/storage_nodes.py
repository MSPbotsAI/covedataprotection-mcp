import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_storage_node(storage_node_info: dict) -> str:
        """Cove Data Protection Management Service method: AddStorageNode.

        JSON-RPC method: AddStorageNode

        Args:
            storage_node_info: Required. Maps to "storageNodeInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeInfo": storage_node_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddStorageNode", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_all_storage_nodes() -> str:
        """Cove Data Protection Management Service method: EnumerateAllStorageNodes.

        JSON-RPC method: EnumerateAllStorageNodes

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAllStorageNodes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_storage_nodes(storage_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateStorageNodes.

        JSON-RPC method: EnumerateStorageNodes

        Args:
            storage_id: Required. Maps to "storageId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageId": storage_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateStorageNodes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_storage_nodes_by_account_id(accounts: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateStorageNodesByAccountId.

        JSON-RPC method: EnumerateStorageNodesByAccountId

        Args:
            accounts: Required. Maps to "accounts" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accounts": accounts}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateStorageNodesByAccountId", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_storage_nodes_with_environments(storage_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateStorageNodesWithEnvironments.

        JSON-RPC method: EnumerateStorageNodesWithEnvironments

        Args:
            storage_id: Required. Maps to "storageId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageId": storage_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateStorageNodesWithEnvironments", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_storage_node_info(storage_node_id: int) -> str:
        """Cove Data Protection Management Service method: GetStorageNodeInfo.

        JSON-RPC method: GetStorageNodeInfo

        Args:
            storage_node_id: Required. Maps to "storageNodeId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeId": storage_node_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetStorageNodeInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_storage_node_info_by_name(storage_id: int, name: str) -> str:
        """Cove Data Protection Management Service method: GetStorageNodeInfoByName.

        JSON-RPC method: GetStorageNodeInfoByName

        Args:
            storage_id: Required. Maps to "storageId" (int).
            name: Required. Maps to "name" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageId": storage_id, "name": name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetStorageNodeInfoByName", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_storage_node_update_info(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetStorageNodeUpdateInfo.

        JSON-RPC method: GetStorageNodeUpdateInfo

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetStorageNodeUpdateInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_storage_node(storage_node_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveStorageNode.

        JSON-RPC method: RemoveStorageNode

        Args:
            storage_node_id: Required. Maps to "storageNodeId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeId": storage_node_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveStorageNode", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_report_storage_node_environment(storage_node_environment_info: dict) -> str:
        """Cove Data Protection Management Service method: ReportStorageNodeEnvironment.

        JSON-RPC method: ReportStorageNodeEnvironment

        Args:
            storage_node_environment_info: Required. Maps to "storageNodeEnvironmentInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeEnvironmentInfo": storage_node_environment_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ReportStorageNodeEnvironment", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_resolve_storage_node_executor(partner_name: str, storage_name: str, storage_node_name: str) -> str:
        """Cove Data Protection Management Service method: ResolveStorageNodeExecutor.

        JSON-RPC method: ResolveStorageNodeExecutor

        Args:
            partner_name: Required. Maps to "partnerName" (str).
            storage_name: Required. Maps to "storageName" (str).
            storage_node_name: Required. Maps to "storageNodeName" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerName": partner_name, "storageName": storage_name, "storageNodeName": storage_node_name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ResolveStorageNodeExecutor", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_update_storage_node(storage_node_id: int, update_with: dict) -> str:
        """Cove Data Protection Management Service method: UpdateStorageNode.

        JSON-RPC method: UpdateStorageNode

        Args:
            storage_node_id: Required. Maps to "storageNodeId" (int).
            update_with: Required. Maps to "updateWith" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeId": storage_node_id, "updateWith": update_with}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UpdateStorageNode", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_update_storage_node_mode(storage_node_id: int, storage_node_mode_info: dict) -> str:
        """Cove Data Protection Management Service method: UpdateStorageNodeMode.

        JSON-RPC method: UpdateStorageNodeMode

        Args:
            storage_node_id: Required. Maps to "storageNodeId" (int).
            storage_node_mode_info: Required. Maps to "storageNodeModeInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeId": storage_node_id, "storageNodeModeInfo": storage_node_mode_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UpdateStorageNodeMode", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_update_storage_node_state(storage_node_id: int, storage_node_state_info: dict) -> str:
        """Cove Data Protection Management Service method: UpdateStorageNodeState.

        JSON-RPC method: UpdateStorageNodeState

        Args:
            storage_node_id: Required. Maps to "storageNodeId" (int).
            storage_node_state_info: Required. Maps to "storageNodeStateInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeId": storage_node_id, "storageNodeStateInfo": storage_node_state_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UpdateStorageNodeState", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
