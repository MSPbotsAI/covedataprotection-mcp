import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_enumerate_audit_action_entity_types() -> str:
        """Cove Data Protection Management Service method: EnumerateAuditActionEntityTypes.

        JSON-RPC method: EnumerateAuditActionEntityTypes

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAuditActionEntityTypes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_audit_action_operation_types() -> str:
        """Cove Data Protection Management Service method: EnumerateAuditActionOperationTypes.

        JSON-RPC method: EnumerateAuditActionOperationTypes

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAuditActionOperationTypes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_audit_action_result_types() -> str:
        """Cove Data Protection Management Service method: EnumerateAuditActionResultTypes.

        JSON-RPC method: EnumerateAuditActionResultTypes

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAuditActionResultTypes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_audit_actions(action_info: dict, from_: int, to: int, count_limit: int, include_all_sub_partners: bool, reverse_order: bool) -> str:
        """Cove Data Protection Management Service method: EnumerateAuditActions.

        JSON-RPC method: EnumerateAuditActions

        Args:
            action_info: Required. Maps to "actionInfo" (dict).
            from_: Required. Maps to "from" (int).
            to: Required. Maps to "to" (int).
            count_limit: Required. Maps to "countLimit" (int).
            include_all_sub_partners: Required. Maps to "includeAllSubPartners" (bool).
            reverse_order: Required. Maps to "reverseOrder" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"actionInfo": action_info, "from": from_, "to": to, "countLimit": count_limit, "includeAllSubPartners": include_all_sub_partners, "reverseOrder": reverse_order}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAuditActions", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
