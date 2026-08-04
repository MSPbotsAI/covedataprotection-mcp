import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:
    @mcp.tool()
    async def covedataprotection_add_partner(partner_info: dict, create_default_account: bool) -> str:
        """Cove Data Protection Management Service method: AddPartner.

        JSON-RPC method: AddPartner

        Args:
            partner_info: Required. Maps to "partnerInfo" (dict).
            create_default_account: Required. Maps to "createDefaultAccount" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerInfo": partner_info, "createDefaultAccount": create_default_account}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddPartner", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_child_partners(partner_id: int, fields: dict, partner_filter: dict, range: dict | None = None) -> str:
        """Cove Data Protection Management Service method: EnumerateChildPartners.

        JSON-RPC method: EnumerateChildPartners

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            fields: Required. Maps to "fields" (dict).
            partner_filter: Required. Maps to "partnerFilter" (dict).
            range: Optional. Maps to "range" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "fields": fields, "partnerFilter": partner_filter, "range": range}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateChildPartners", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_partners(parent_partner_id: int, fetch_recursively: bool, fields: dict) -> str:
        """Cove Data Protection Management Service method: EnumeratePartners.

        JSON-RPC method: EnumeratePartners

        Args:
            parent_partner_id: Required. Maps to "parentPartnerId" (int).
            fetch_recursively: Required. Maps to "fetchRecursively" (bool).
            fields: Required. Maps to "fields" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"parentPartnerId": parent_partner_id, "fetchRecursively": fetch_recursively, "fields": fields}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePartners", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_info(name: str) -> str:
        """Cove Data Protection Management Service method: GetPartnerInfo.

        JSON-RPC method: GetPartnerInfo

        Args:
            name: Required. Maps to "name" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"name": name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_info_by_id(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerInfoById.

        JSON-RPC method: GetPartnerInfoById

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerInfoById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_tree(partner_id: int, fields: dict, filter: str, children_limit: int, partner_filter: dict) -> str:
        """Cove Data Protection Management Service method: GetPartnerTree.

        JSON-RPC method: GetPartnerTree

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            fields: Required. Maps to "fields" (dict).
            filter: Required. Maps to "filter" (str).
            children_limit: Required. Maps to "childrenLimit" (int).
            partner_filter: Required. Maps to "partnerFilter" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "fields": fields, "filter": filter, "childrenLimit": children_limit, "partnerFilter": partner_filter}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerTree", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_root_partner_name() -> str:
        """Cove Data Protection Management Service method: GetRootPartnerName.

        JSON-RPC method: GetRootPartnerName

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetRootPartnerName", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_partner(partner_info: dict, force_remove_custom_column_values_in_old_scope: bool) -> str:
        """Cove Data Protection Management Service method: ModifyPartner.

        JSON-RPC method: ModifyPartner

        Args:
            partner_info: Required. Maps to "partnerInfo" (dict).
            force_remove_custom_column_values_in_old_scope: Required. Maps to "forceRemoveCustomColumnValuesInOldScope" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerInfo": partner_info, "forceRemoveCustomColumnValuesInOldScope": force_remove_custom_column_values_in_old_scope}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyPartner", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_partner(partner_id: int) -> str:
        """Cove Data Protection Management Service method: RemovePartner.

        JSON-RPC method: RemovePartner

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemovePartner", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

