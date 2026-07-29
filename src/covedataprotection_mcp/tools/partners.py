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
    async def covedataprotection_add_partner_ex(partner_info: dict, create_default_account: bool) -> str:
        """Cove Data Protection Management Service method: AddPartnerEx.

        JSON-RPC method: AddPartnerEx

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
            result = await client.call("AddPartnerEx", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_change_partner_state(partner_id: int, action: str, reason: str) -> str:
        """Cove Data Protection Management Service method: ChangePartnerState.

        JSON-RPC method: ChangePartnerState

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            action: Required. Maps to "action" (str).
            reason: Required. Maps to "reason" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "action": action, "reason": reason}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ChangePartnerState", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_partner_id_tree(account_name: str, account_password: str) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountPartnerIdTree.

        JSON-RPC method: EnumerateAccountPartnerIdTree

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
            result = await client.call("EnumerateAccountPartnerIdTree", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_advanced_partner_properties_infos(parent_partner_id: int, fetch_recursively: bool) -> str:
        """Cove Data Protection Management Service method: EnumerateAdvancedPartnerPropertiesInfos.

        JSON-RPC method: EnumerateAdvancedPartnerPropertiesInfos

        Args:
            parent_partner_id: Required. Maps to "parentPartnerId" (int).
            fetch_recursively: Required. Maps to "fetchRecursively" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"parentPartnerId": parent_partner_id, "fetchRecursively": fetch_recursively}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAdvancedPartnerPropertiesInfos", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_advanced_partner_properties_infos_by_partner_ids(partner_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateAdvancedPartnerPropertiesInfosByPartnerIds.

        JSON-RPC method: EnumerateAdvancedPartnerPropertiesInfosByPartnerIds

        Args:
            partner_ids: Required. Maps to "partnerIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerIds": partner_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAdvancedPartnerPropertiesInfosByPartnerIds", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_ancestor_partners(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateAncestorPartners.

        JSON-RPC method: EnumerateAncestorPartners

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAncestorPartners", params)
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
    async def covedataprotection_enumerate_external_partner_properties(partner_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateExternalPartnerProperties.

        JSON-RPC method: EnumerateExternalPartnerProperties

        Args:
            partner_ids: Required. Maps to "partnerIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerIds": partner_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateExternalPartnerProperties", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_partner_properties() -> str:
        """Cove Data Protection Management Service method: EnumeratePartnerProperties.

        JSON-RPC method: EnumeratePartnerProperties

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePartnerProperties", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_partner_state_transitions() -> str:
        """Cove Data Protection Management Service method: EnumeratePartnerStateTransitions.

        JSON-RPC method: EnumeratePartnerStateTransitions

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePartnerStateTransitions", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_partner_states_by_period(start_time: int, end_time: int) -> str:
        """Cove Data Protection Management Service method: EnumeratePartnerStatesByPeriod.

        JSON-RPC method: EnumeratePartnerStatesByPeriod

        Args:
            start_time: Required. Maps to "startTime" (int).
            end_time: Required. Maps to "endTime" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"startTime": start_time, "endTime": end_time}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePartnerStatesByPeriod", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_partner_urls(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumeratePartnerUrls.

        JSON-RPC method: EnumeratePartnerUrls

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePartnerUrls", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_partner_users_login_times(partner_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumeratePartnerUsersLoginTimes.

        JSON-RPC method: EnumeratePartnerUsersLoginTimes

        Args:
            partner_ids: Required. Maps to "partnerIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerIds": partner_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePartnerUsersLoginTimes", params)
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
    async def covedataprotection_enumerate_partners_at_time(parent_partner_id: int, fetch_recursively: bool, time: int) -> str:
        """Cove Data Protection Management Service method: EnumeratePartnersAtTime.

        JSON-RPC method: EnumeratePartnersAtTime

        Args:
            parent_partner_id: Required. Maps to "parentPartnerId" (int).
            fetch_recursively: Required. Maps to "fetchRecursively" (bool).
            time: Required. Maps to "time" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"parentPartnerId": parent_partner_id, "fetchRecursively": fetch_recursively, "time": time}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePartnersAtTime", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_permitted_partners(entity: str, action: str, partner_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumeratePermittedPartners.

        JSON-RPC method: EnumeratePermittedPartners

        Args:
            entity: Required. Maps to "entity" (str).
            action: Required. Maps to "action" (str).
            partner_ids: Required. Maps to "partnerIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"entity": entity, "action": action, "partnerIds": partner_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumeratePermittedPartners", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_removed_partners(parent_partner_id: int, start_time: int, end_time: int) -> str:
        """Cove Data Protection Management Service method: EnumerateRemovedPartners.

        JSON-RPC method: EnumerateRemovedPartners

        Args:
            parent_partner_id: Required. Maps to "parentPartnerId" (int).
            start_time: Required. Maps to "startTime" (int).
            end_time: Required. Maps to "endTime" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"parentPartnerId": parent_partner_id, "startTime": start_time, "endTime": end_time}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateRemovedPartners", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_respect_removed_ancestor_partners_at_time(partner_id: int, time: int) -> str:
        """Cove Data Protection Management Service method: EnumerateRespectRemovedAncestorPartnersAtTime.

        JSON-RPC method: EnumerateRespectRemovedAncestorPartnersAtTime

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            time: Required. Maps to "time" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "time": time}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateRespectRemovedAncestorPartnersAtTime", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_unique_partner_states_by_period(start_time: int, end_time: int) -> str:
        """Cove Data Protection Management Service method: EnumerateUniquePartnerStatesByPeriod.

        JSON-RPC method: EnumerateUniquePartnerStatesByPeriod

        Args:
            start_time: Required. Maps to "startTime" (int).
            end_time: Required. Maps to "endTime" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"startTime": start_time, "endTime": end_time}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateUniquePartnerStatesByPeriod", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_advanced_partner_properties(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetAdvancedPartnerProperties.

        JSON-RPC method: GetAdvancedPartnerProperties

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAdvancedPartnerProperties", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_auto_deployment_partner_state(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetAutoDeploymentPartnerState.

        JSON-RPC method: GetAutoDeploymentPartnerState

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAutoDeploymentPartnerState", params)
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
    async def covedataprotection_get_partner_info_at_time(partner_id: int, time: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerInfoAtTime.

        JSON-RPC method: GetPartnerInfoAtTime

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            time: Required. Maps to "time" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "time": time}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerInfoAtTime", params)
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
    async def covedataprotection_get_partner_info_by_uid(partner_uid: str) -> str:
        """Cove Data Protection Management Service method: GetPartnerInfoByUid.

        JSON-RPC method: GetPartnerInfoByUid

        Args:
            partner_uid: Required. Maps to "partnerUid" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerUid": partner_uid}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerInfoByUid", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_info_history(partner_id: int, fields: dict) -> str:
        """Cove Data Protection Management Service method: GetPartnerInfoHistory.

        JSON-RPC method: GetPartnerInfoHistory

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            fields: Required. Maps to "fields" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "fields": fields}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerInfoHistory", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_price_currency(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerPriceCurrency.

        JSON-RPC method: GetPartnerPriceCurrency

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerPriceCurrency", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_production_dates(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerProductionDates.

        JSON-RPC method: GetPartnerProductionDates

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerProductionDates", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_state(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerState.

        JSON-RPC method: GetPartnerState

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerState", params)
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
    async def covedataprotection_get_partner_url(partner_id: int, url_type: str) -> str:
        """Cove Data Protection Management Service method: GetPartnerUrl.

        JSON-RPC method: GetPartnerUrl

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            url_type: Required. Maps to "urlType" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "urlType": url_type}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerUrl", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_users_login_times(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerUsersLoginTimes.

        JSON-RPC method: GetPartnerUsersLoginTimes

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerUsersLoginTimes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partners_rule_applied_to(rule_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnersRuleAppliedTo.

        JSON-RPC method: GetPartnersRuleAppliedTo

        Args:
            rule_id: Required. Maps to "ruleId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"ruleId": rule_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnersRuleAppliedTo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partners_rule_inactive_for(rule_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnersRuleInactiveFor.

        JSON-RPC method: GetPartnersRuleInactiveFor

        Args:
            rule_id: Required. Maps to "ruleId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"ruleId": rule_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnersRuleInactiveFor", params)
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
    async def covedataprotection_is_auto_deployment_allowed_for_partner(partner_id: int) -> str:
        """Cove Data Protection Management Service method: IsAutoDeploymentAllowedForPartner.

        JSON-RPC method: IsAutoDeploymentAllowedForPartner

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("IsAutoDeploymentAllowedForPartner", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_is_direct_debtor_partner(partner_id: int) -> str:
        """Cove Data Protection Management Service method: IsDirectDebtorPartner.

        JSON-RPC method: IsDirectDebtorPartner

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("IsDirectDebtorPartner", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_auto_deployment_partner_state(partner_id: int, auto_deployment_state: str) -> str:
        """Cove Data Protection Management Service method: ModifyAutoDeploymentPartnerState.

        JSON-RPC method: ModifyAutoDeploymentPartnerState

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            auto_deployment_state: Required. Maps to "autoDeploymentState" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "autoDeploymentState": auto_deployment_state}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyAutoDeploymentPartnerState", params)
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
    async def covedataprotection_regenerate_partner_uid(partner_id: int) -> str:
        """Cove Data Protection Management Service method: RegeneratePartnerUid.

        JSON-RPC method: RegeneratePartnerUid

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RegeneratePartnerUid", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_register_external_partner_property(partner_property: dict) -> str:
        """Cove Data Protection Management Service method: RegisterExternalPartnerProperty.

        JSON-RPC method: RegisterExternalPartnerProperty

        Args:
            partner_property: Required. Maps to "partnerProperty" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerProperty": partner_property}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RegisterExternalPartnerProperty", params)
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

    @mcp.tool()
    async def covedataprotection_set_advanced_partner_properties(partner_id: int, advanced_partner_properties_info: dict) -> str:
        """Cove Data Protection Management Service method: SetAdvancedPartnerProperties.

        JSON-RPC method: SetAdvancedPartnerProperties

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            advanced_partner_properties_info: Required. Maps to "advancedPartnerPropertiesInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "advancedPartnerPropertiesInfo": advanced_partner_properties_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetAdvancedPartnerProperties", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_partner_price_currency(partner_id: int, currency: str) -> str:
        """Cove Data Protection Management Service method: SetPartnerPriceCurrency.

        JSON-RPC method: SetPartnerPriceCurrency

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            currency: Required. Maps to "currency" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "currency": currency}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetPartnerPriceCurrency", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_partner_url(partner_id: int, url_type: str, url: str) -> str:
        """Cove Data Protection Management Service method: SetPartnerUrl.

        JSON-RPC method: SetPartnerUrl

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            url_type: Required. Maps to "urlType" (str).
            url: Required. Maps to "url" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "urlType": url_type, "url": url}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetPartnerUrl", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
