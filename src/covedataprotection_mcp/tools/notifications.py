import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_notification_rule(rule: dict) -> str:
        """Cove Data Protection Management Service method: AddNotificationRule.

        JSON-RPC method: AddNotificationRule

        Args:
            rule: Required. Maps to "rule" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"rule": rule}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddNotificationRule", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_add_notification_template(notification_template: dict) -> str:
        """Cove Data Protection Management Service method: AddNotificationTemplate.

        JSON-RPC method: AddNotificationTemplate

        Args:
            notification_template: Required. Maps to "notificationTemplate" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"notificationTemplate": notification_template}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddNotificationTemplate", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_add_notification_transport(transport: dict) -> str:
        """Cove Data Protection Management Service method: AddNotificationTransport.

        JSON-RPC method: AddNotificationTransport

        Args:
            transport: Required. Maps to "transport" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"transport": transport}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddNotificationTransport", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enable_notification_rule(rule_id: int, partner_id: int, enable: bool) -> str:
        """Cove Data Protection Management Service method: EnableNotificationRule.

        JSON-RPC method: EnableNotificationRule

        Args:
            rule_id: Required. Maps to "ruleId" (int).
            partner_id: Required. Maps to "partnerId" (int).
            enable: Required. Maps to "enable" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"ruleId": rule_id, "partnerId": partner_id, "enable": enable}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnableNotificationRule", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_all_active_notification_rules() -> str:
        """Cove Data Protection Management Service method: EnumerateAllActiveNotificationRules.

        JSON-RPC method: EnumerateAllActiveNotificationRules

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAllActiveNotificationRules", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_all_inactive_notification_rules() -> str:
        """Cove Data Protection Management Service method: EnumerateAllInactiveNotificationRules.

        JSON-RPC method: EnumerateAllInactiveNotificationRules

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAllInactiveNotificationRules", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_all_notification_rules() -> str:
        """Cove Data Protection Management Service method: EnumerateAllNotificationRules.

        JSON-RPC method: EnumerateAllNotificationRules

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAllNotificationRules", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_all_notification_transports() -> str:
        """Cove Data Protection Management Service method: EnumerateAllNotificationTransports.

        JSON-RPC method: EnumerateAllNotificationTransports

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAllNotificationTransports", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_notification_rules(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateNotificationRules.

        JSON-RPC method: EnumerateNotificationRules

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateNotificationRules", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_notification_transports(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateNotificationTransports.

        JSON-RPC method: EnumerateNotificationTransports

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateNotificationTransports", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_unsubscribed_emails(entity: str) -> str:
        """Cove Data Protection Management Service method: EnumerateUnsubscribedEmails.

        JSON-RPC method: EnumerateUnsubscribedEmails

        Args:
            entity: Required. Maps to "entity" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"entity": entity}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateUnsubscribedEmails", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_notification_rule(id: int) -> str:
        """Cove Data Protection Management Service method: GetNotificationRule.

        JSON-RPC method: GetNotificationRule

        Args:
            id: Required. Maps to "id" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"id": id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetNotificationRule", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_notification_template(id: int) -> str:
        """Cove Data Protection Management Service method: GetNotificationTemplate.

        JSON-RPC method: GetNotificationTemplate

        Args:
            id: Required. Maps to "id" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"id": id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetNotificationTemplate", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_notification_transport(id: int) -> str:
        """Cove Data Protection Management Service method: GetNotificationTransport.

        JSON-RPC method: GetNotificationTransport

        Args:
            id: Required. Maps to "id" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"id": id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetNotificationTransport", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_notification_template(template_id: int, partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerNotificationTemplate.

        JSON-RPC method: GetPartnerNotificationTemplate

        Args:
            template_id: Required. Maps to "templateId" (int).
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"templateId": template_id, "partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerNotificationTemplate", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_notification_rule(rule: dict) -> str:
        """Cove Data Protection Management Service method: ModifyNotificationRule.

        JSON-RPC method: ModifyNotificationRule

        Args:
            rule: Required. Maps to "rule" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"rule": rule}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyNotificationRule", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_notification_template(notification_template: dict) -> str:
        """Cove Data Protection Management Service method: ModifyNotificationTemplate.

        JSON-RPC method: ModifyNotificationTemplate

        Args:
            notification_template: Required. Maps to "notificationTemplate" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"notificationTemplate": notification_template}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyNotificationTemplate", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_notification_transport(transport: dict) -> str:
        """Cove Data Protection Management Service method: ModifyNotificationTransport.

        JSON-RPC method: ModifyNotificationTransport

        Args:
            transport: Required. Maps to "transport" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"transport": transport}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyNotificationTransport", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_notification_rule(id: int) -> str:
        """Cove Data Protection Management Service method: RemoveNotificationRule.

        JSON-RPC method: RemoveNotificationRule

        Args:
            id: Required. Maps to "id" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"id": id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveNotificationRule", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_notification_template(id: int) -> str:
        """Cove Data Protection Management Service method: RemoveNotificationTemplate.

        JSON-RPC method: RemoveNotificationTemplate

        Args:
            id: Required. Maps to "id" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"id": id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveNotificationTemplate", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_notification_transport(id: int) -> str:
        """Cove Data Protection Management Service method: RemoveNotificationTransport.

        JSON-RPC method: RemoveNotificationTransport

        Args:
            id: Required. Maps to "id" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"id": id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveNotificationTransport", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_unsubscribe_email_from_rule(token: str) -> str:
        """Cove Data Protection Management Service method: UnsubscribeEmailFromRule.

        JSON-RPC method: UnsubscribeEmailFromRule

        Args:
            token: Required. Maps to "token" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"token": token}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UnsubscribeEmailFromRule", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_unsubscribe_view_delivery(token: str) -> str:
        """Cove Data Protection Management Service method: UnsubscribeViewDelivery.

        JSON-RPC method: UnsubscribeViewDelivery

        Args:
            token: Required. Maps to "token" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"token": token}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UnsubscribeViewDelivery", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
