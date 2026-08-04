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

