import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_find_branding(partner_id: int, application_type: str) -> str:
        """Cove Data Protection Management Service method: FindBranding.

        JSON-RPC method: FindBranding

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            application_type: Required. Maps to "applicationType" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "applicationType": application_type}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("FindBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_effective_partner_branding(application_type: str) -> str:
        """Cove Data Protection Management Service method: GetEffectivePartnerBranding.

        JSON-RPC method: GetEffectivePartnerBranding

        Args:
            application_type: Required. Maps to "applicationType" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"applicationType": application_type}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetEffectivePartnerBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_branding(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerBranding.

        JSON-RPC method: GetPartnerBranding

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_partner_web_branding(partner_id: int) -> str:
        """Cove Data Protection Management Service method: GetPartnerWebBranding.

        JSON-RPC method: GetPartnerWebBranding

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetPartnerWebBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_reset_branding(partner_id: int, application_type: str) -> str:
        """Cove Data Protection Management Service method: ResetBranding.

        JSON-RPC method: ResetBranding

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            application_type: Required. Maps to "applicationType" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "applicationType": application_type}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ResetBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_branding(partner_id: int, application_type: str, branding_body: list) -> str:
        """Cove Data Protection Management Service method: SetBranding.

        JSON-RPC method: SetBranding

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            application_type: Required. Maps to "applicationType" (str).
            branding_body: Required. Maps to "brandingBody" (list).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "applicationType": application_type, "brandingBody": branding_body}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_partner_branding(partner_id: int, branding_archive: dict) -> str:
        """Cove Data Protection Management Service method: SetPartnerBranding.

        JSON-RPC method: SetPartnerBranding

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            branding_archive: Required. Maps to "brandingArchive" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "brandingArchive": branding_archive}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetPartnerBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_set_partner_web_branding(partner_id: int, web_branding_archive: dict) -> str:
        """Cove Data Protection Management Service method: SetPartnerWebBranding.

        JSON-RPC method: SetPartnerWebBranding

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            web_branding_archive: Required. Maps to "webBrandingArchive" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "webBrandingArchive": web_branding_archive}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("SetPartnerWebBranding", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
