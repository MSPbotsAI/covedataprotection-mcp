import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_user(user_info: dict) -> str:
        """Cove Data Protection Management Service method: AddUser.

        JSON-RPC method: AddUser

        Args:
            user_info: Required. Maps to "userInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userInfo": user_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddUser", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_add_user_settings(user_settings: dict) -> str:
        """Cove Data Protection Management Service method: AddUserSettings.

        JSON-RPC method: AddUserSettings

        Args:
            user_settings: Required. Maps to "userSettings" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userSettings": user_settings}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddUserSettings", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_user_roles() -> str:
        """Cove Data Protection Management Service method: EnumerateUserRoles.

        JSON-RPC method: EnumerateUserRoles

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateUserRoles", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_user_settings(user_id: int | None = None, settings_type: str | None = None) -> str:
        """Cove Data Protection Management Service method: EnumerateUserSettings.

        JSON-RPC method: EnumerateUserSettings

        Args:
            user_id: Optional. Maps to "userId" (int).
            settings_type: Optional. Maps to "settingsType" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userId": user_id, "settingsType": settings_type}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateUserSettings", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_users(partner_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateUsers.

        JSON-RPC method: EnumerateUsers

        Args:
            partner_ids: Required. Maps to "partnerIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerIds": partner_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateUsers", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_users_by_filter(filter: dict) -> str:
        """Cove Data Protection Management Service method: EnumerateUsersByFilter.

        JSON-RPC method: EnumerateUsersByFilter

        Args:
            filter: Required. Maps to "filter" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"filter": filter}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateUsersByFilter", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_users_with_security_officer_flag(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateUsersWithSecurityOfficerFlag.

        JSON-RPC method: EnumerateUsersWithSecurityOfficerFlag

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateUsersWithSecurityOfficerFlag", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_respect_removed_user_info_by_id(user_id: int) -> str:
        """Cove Data Protection Management Service method: GetRespectRemovedUserInfoById.

        JSON-RPC method: GetRespectRemovedUserInfoById

        Args:
            user_id: Required. Maps to "userId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userId": user_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetRespectRemovedUserInfoById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_user_info(partner_id: int, name_or_email: str, password: str) -> str:
        """Cove Data Protection Management Service method: GetUserInfo.

        JSON-RPC method: GetUserInfo

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            name_or_email: Required. Maps to "nameOrEmail" (str).
            password: Required. Maps to "password" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "nameOrEmail": name_or_email, "password": password}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetUserInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_user_info_by_id(user_id: int) -> str:
        """Cove Data Protection Management Service method: GetUserInfoById.

        JSON-RPC method: GetUserInfoById

        Args:
            user_id: Required. Maps to "userId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userId": user_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetUserInfoById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_user_passport(user_id: int, authentication_context: dict) -> str:
        """Cove Data Protection Management Service method: GetUserPassport.

        JSON-RPC method: GetUserPassport

        Args:
            user_id: Required. Maps to "userId" (int).
            authentication_context: Required. Maps to "authenticationContext" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userId": user_id, "authenticationContext": authentication_context}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetUserPassport", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_user_settings(settings_id: int) -> str:
        """Cove Data Protection Management Service method: GetUserSettings.

        JSON-RPC method: GetUserSettings

        Args:
            settings_id: Required. Maps to "settingsId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"settingsId": settings_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetUserSettings", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_user(user_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyUser.

        JSON-RPC method: ModifyUser

        Args:
            user_info: Required. Maps to "userInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userInfo": user_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyUser", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_user_on_login(user_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyUserOnLogin.

        JSON-RPC method: ModifyUserOnLogin

        Args:
            user_info: Required. Maps to "userInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userInfo": user_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyUserOnLogin", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_user_settings(user_settings: dict) -> str:
        """Cove Data Protection Management Service method: ModifyUserSettings.

        JSON-RPC method: ModifyUserSettings

        Args:
            user_settings: Required. Maps to "userSettings" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userSettings": user_settings}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyUserSettings", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_user(user_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveUser.

        JSON-RPC method: RemoveUser

        Args:
            user_id: Required. Maps to "userId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userId": user_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveUser", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_user_settings(settings_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveUserSettings.

        JSON-RPC method: RemoveUserSettings

        Args:
            settings_id: Required. Maps to "settingsId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"settingsId": settings_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveUserSettings", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_send_user_invitation(receiver_user_id: int, redeem_link: str, inviter_user_id: int | None = None) -> str:
        """Cove Data Protection Management Service method: SendUserInvitation.

        JSON-RPC method: SendUserInvitation

        Args:
            receiver_user_id: Required. Maps to "receiverUserId" (int).
            redeem_link: Required. Maps to "redeemLink" (str).
            inviter_user_id: Optional. Maps to "inviterUserId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"receiverUserId": receiver_user_id, "redeemLink": redeem_link, "inviterUserId": inviter_user_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SendUserInvitation", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_current_user_settings(current_user_settings_info: dict) -> str:
        """Cove Data Protection Management Service method: SetCurrentUserSettings.

        JSON-RPC method: SetCurrentUserSettings

        Args:
            current_user_settings_info: Required. Maps to "currentUserSettingsInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"currentUserSettingsInfo": current_user_settings_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetCurrentUserSettings", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
