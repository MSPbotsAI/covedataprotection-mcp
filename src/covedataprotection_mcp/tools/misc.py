import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_invitation_link(partner_id: int, invitation_link: str) -> str:
        """Cove Data Protection Management Service method: AddInvitationLink.

        JSON-RPC method: AddInvitationLink

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            invitation_link: Required. Maps to "invitationLink" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "invitationLink": invitation_link}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddInvitationLink", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_end_customer_prices(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateEndCustomerPrices.

        JSON-RPC method: EnumerateEndCustomerPrices

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateEndCustomerPrices", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_generate_reinstallation_passphrase(account_id: int) -> str:
        """Cove Data Protection Management Service method: GenerateReinstallationPassphrase.

        JSON-RPC method: GenerateReinstallationPassphrase

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GenerateReinstallationPassphrase", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_auto_deploy_command_line(partner_id: int, profile_name: str | None = None) -> str:
        """Cove Data Protection Management Service method: GetAutoDeployCommandLine.

        JSON-RPC method: GetAutoDeployCommandLine

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            profile_name: Optional. Maps to "profileName" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "profileName": profile_name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAutoDeployCommandLine", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_auto_login_url(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetAutoLoginUrl.

        JSON-RPC method: GetAutoLoginUrl

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetAutoLoginUrl", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_common_statistics_by_token(token: str) -> str:
        """Cove Data Protection Management Service method: GetCommonStatisticsByToken.

        JSON-RPC method: GetCommonStatisticsByToken

        Args:
            token: Required. Maps to "token" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"token": token}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetCommonStatisticsByToken", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_effective_environment_info() -> str:
        """Cove Data Protection Management Service method: GetEffectiveEnvironmentInfo.

        JSON-RPC method: GetEffectiveEnvironmentInfo

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetEffectiveEnvironmentInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_encryption_key_by_passphrase(account_id: int, passphrase: str) -> str:
        """Cove Data Protection Management Service method: GetEncryptionKeyByPassphrase.

        JSON-RPC method: GetEncryptionKeyByPassphrase

        Args:
            account_id: Required. Maps to "accountId" (int).
            passphrase: Required. Maps to "passphrase" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id, "passphrase": passphrase}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetEncryptionKeyByPassphrase", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_remote_client_connection_locator(account_id: int) -> str:
        """Cove Data Protection Management Service method: GetRemoteClientConnectionLocator.

        JSON-RPC method: GetRemoteClientConnectionLocator

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetRemoteClientConnectionLocator", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_server_info() -> str:
        """Cove Data Protection Management Service method: GetServerInfo.

        JSON-RPC method: GetServerInfo

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetServerInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_is_sims_plugin_enabled(partner_id: int) -> str:
        """Cove Data Protection Management Service method: IsSimsPluginEnabled.

        JSON-RPC method: IsSimsPluginEnabled

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("IsSimsPluginEnabled", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_is_sims_plugin_enabled_for_any_child(partner_id: int) -> str:
        """Cove Data Protection Management Service method: IsSimsPluginEnabledForAnyChild.

        JSON-RPC method: IsSimsPluginEnabledForAnyChild

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("IsSimsPluginEnabledForAnyChild", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_lookup_transport(partner_id: int, transport_type: str) -> str:
        """Cove Data Protection Management Service method: LookupTransport.

        JSON-RPC method: LookupTransport

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            transport_type: Required. Maps to "transportType" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "transportType": transport_type}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("LookupTransport", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_personal_data(partner_id: int, from_timestamp: int | None = None, to_timestamp: int | None = None) -> str:
        """Cove Data Protection Management Service method: RemovePersonalData.

        JSON-RPC method: RemovePersonalData

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            from_timestamp: Optional. Maps to "fromTimestamp" (int).
            to_timestamp: Optional. Maps to "toTimestamp" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "fromTimestamp": from_timestamp, "toTimestamp": to_timestamp}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemovePersonalData", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_end_customer_price(partner_id: int, end_customer_price: dict) -> str:
        """Cove Data Protection Management Service method: SetEndCustomerPrice.

        JSON-RPC method: SetEndCustomerPrice

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            end_customer_price: Required. Maps to "endCustomerPrice" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "endCustomerPrice": end_customer_price}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetEndCustomerPrice", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_update_statistics(posting: dict) -> str:
        """Cove Data Protection Management Service method: UpdateStatistics.

        JSON-RPC method: UpdateStatistics

        Args:
            posting: Required. Maps to "posting" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"posting": posting}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("UpdateStatistics", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_verify_encryption_key(account_id: int, encryption_key: str) -> str:
        """Cove Data Protection Management Service method: VerifyEncryptionKey.

        JSON-RPC method: VerifyEncryptionKey

        Args:
            account_id: Required. Maps to "accountId" (int).
            encryption_key: Required. Maps to "encryptionKey" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id, "encryptionKey": encryption_key}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("VerifyEncryptionKey", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
