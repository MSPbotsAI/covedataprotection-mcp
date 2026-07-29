import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_view_delivery(view_delivery_info: dict) -> str:
        """Cove Data Protection Management Service method: AddViewDelivery.

        JSON-RPC method: AddViewDelivery

        Args:
            view_delivery_info: Required. Maps to "viewDeliveryInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"viewDeliveryInfo": view_delivery_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddViewDelivery", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_view_deliveries(user_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateViewDeliveries.

        JSON-RPC method: EnumerateViewDeliveries

        Args:
            user_id: Required. Maps to "userId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userId": user_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateViewDeliveries", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_view_delivery_external_recipients_states(view_delivery_id: int) -> str:
        """Cove Data Protection Management Service method: GetViewDeliveryExternalRecipientsStates.

        JSON-RPC method: GetViewDeliveryExternalRecipientsStates

        Args:
            view_delivery_id: Required. Maps to "viewDeliveryId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"viewDeliveryId": view_delivery_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetViewDeliveryExternalRecipientsStates", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_view_delivery_info_by_id(view_delivery_id: int) -> str:
        """Cove Data Protection Management Service method: GetViewDeliveryInfoById.

        JSON-RPC method: GetViewDeliveryInfoById

        Args:
            view_delivery_id: Required. Maps to "viewDeliveryId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"viewDeliveryId": view_delivery_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetViewDeliveryInfoById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_view_delivery_recipients_states(view_delivery_id: int) -> str:
        """Cove Data Protection Management Service method: GetViewDeliveryRecipientsStates.

        JSON-RPC method: GetViewDeliveryRecipientsStates

        Args:
            view_delivery_id: Required. Maps to "viewDeliveryId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"viewDeliveryId": view_delivery_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetViewDeliveryRecipientsStates", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_is_view_delivery_enabled(partner_id: int) -> str:
        """Cove Data Protection Management Service method: IsViewDeliveryEnabled.

        JSON-RPC method: IsViewDeliveryEnabled

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("IsViewDeliveryEnabled", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_view_delivery(view_delivery_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyViewDelivery.

        JSON-RPC method: ModifyViewDelivery

        Args:
            view_delivery_info: Required. Maps to "viewDeliveryInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"viewDeliveryInfo": view_delivery_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyViewDelivery", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_opt_in_view_delivery(token: str) -> str:
        """Cove Data Protection Management Service method: OptInViewDelivery.

        JSON-RPC method: OptInViewDelivery

        Args:
            token: Required. Maps to "token" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"token": token}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("OptInViewDelivery", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_perform_view_delivery(view_delivery_id: int) -> str:
        """Cove Data Protection Management Service method: PerformViewDelivery.

        JSON-RPC method: PerformViewDelivery

        Args:
            view_delivery_id: Required. Maps to "viewDeliveryId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"viewDeliveryId": view_delivery_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("PerformViewDelivery", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_view_delivery(view_delivery_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveViewDelivery.

        JSON-RPC method: RemoveViewDelivery

        Args:
            view_delivery_id: Required. Maps to "viewDeliveryId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"viewDeliveryId": view_delivery_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveViewDelivery", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
