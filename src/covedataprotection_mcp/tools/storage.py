import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_storage(add_storage_info: dict) -> str:
        """Cove Data Protection Management Service method: AddStorage.

        JSON-RPC method: AddStorage

        Args:
            add_storage_info: Required. Maps to "addStorageInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"addStorageInfo": add_storage_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddStorage", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_software_only_ancestral_partners_storages(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateSoftwareOnlyAncestralPartnersStorages.

        JSON-RPC method: EnumerateSoftwareOnlyAncestralPartnersStorages

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateSoftwareOnlyAncestralPartnersStorages", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_storage_statistics(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateStorageStatistics.

        JSON-RPC method: EnumerateStorageStatistics

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateStorageStatistics", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_storages(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateStorages.

        JSON-RPC method: EnumerateStorages

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateStorages", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_reserved_storage(storage_node_id: int) -> str:
        """Cove Data Protection Management Service method: GetReservedStorage.

        JSON-RPC method: GetReservedStorage

        Args:
            storage_node_id: Required. Maps to "storageNodeId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageNodeId": storage_node_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetReservedStorage", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_storage_info(storage_id: int) -> str:
        """Cove Data Protection Management Service method: GetStorageInfo.

        JSON-RPC method: GetStorageInfo

        Args:
            storage_id: Required. Maps to "storageId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageId": storage_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetStorageInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_storage_info_by_name(partner_id: int, name: str) -> str:
        """Cove Data Protection Management Service method: GetStorageInfoByName.

        JSON-RPC method: GetStorageInfoByName

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            name: Required. Maps to "name" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "name": name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetStorageInfoByName", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_storage(storage_id: int, storage_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyStorage.

        JSON-RPC method: ModifyStorage

        Args:
            storage_id: Required. Maps to "storageId" (int).
            storage_info: Required. Maps to "storageInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageId": storage_id, "storageInfo": storage_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyStorage", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_storage(storage_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveStorage.

        JSON-RPC method: RemoveStorage

        Args:
            storage_id: Required. Maps to "storageId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"storageId": storage_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveStorage", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_reserve_storage_on_account_node(node_guid: str, reserved_size: int) -> str:
        """Cove Data Protection Management Service method: ReserveStorageOnAccountNode.

        JSON-RPC method: ReserveStorageOnAccountNode

        Args:
            node_guid: Required. Maps to "nodeGuid" (str).
            reserved_size: Required. Maps to "reservedSize" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"nodeGuid": node_guid, "reservedSize": reserved_size}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ReserveStorageOnAccountNode", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
