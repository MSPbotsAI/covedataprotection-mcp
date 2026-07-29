import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_accept_eula(full_name: str, role: str) -> str:
        """Cove Data Protection Management Service method: AcceptEula.

        JSON-RPC method: AcceptEula

        Args:
            full_name: Required. Maps to "fullName" (str).
            role: Required. Maps to "role" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"fullName": full_name, "role": role}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AcceptEula", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_decline_eula(full_name: str, role: str) -> str:
        """Cove Data Protection Management Service method: DeclineEula.

        JSON-RPC method: DeclineEula

        Args:
            full_name: Required. Maps to "fullName" (str).
            role: Required. Maps to "role" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"fullName": full_name, "role": role}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("DeclineEula", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_common_eula_info() -> str:
        """Cove Data Protection Management Service method: GetCommonEulaInfo.

        JSON-RPC method: GetCommonEulaInfo

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetCommonEulaInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_end_customer_eula_state(user_id: int) -> str:
        """Cove Data Protection Management Service method: GetEndCustomerEulaState.

        JSON-RPC method: GetEndCustomerEulaState

        Args:
            user_id: Required. Maps to "userId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"userId": user_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetEndCustomerEulaState", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_eula_info() -> str:
        """Cove Data Protection Management Service method: GetEulaInfo.

        JSON-RPC method: GetEulaInfo

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetEulaInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_eula_info(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerEulaInfo.

        JSON-RPC method: GetPartnerEulaInfo

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerEulaInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
