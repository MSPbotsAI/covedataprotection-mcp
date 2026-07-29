import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_enumerate_account_remote_access_endpoints(account_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountRemoteAccessEndpoints.

        JSON-RPC method: EnumerateAccountRemoteAccessEndpoints

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountRemoteAccessEndpoints", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_countries() -> str:
        """Cove Data Protection Management Service method: EnumerateCountries.

        JSON-RPC method: EnumerateCountries

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateCountries", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_country_by_iso_code(country_iso_code: str) -> str:
        """Cove Data Protection Management Service method: GetCountryByIsoCode.

        JSON-RPC method: GetCountryByIsoCode

        Args:
            country_iso_code: Required. Maps to "countryIsoCode" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"countryIsoCode": country_iso_code}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetCountryByIsoCode", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_country_by_iso_code_or_name(country_iso_code_or_name: str) -> str:
        """Cove Data Protection Management Service method: GetCountryByIsoCodeOrName.

        JSON-RPC method: GetCountryByIsoCodeOrName

        Args:
            country_iso_code_or_name: Required. Maps to "countryIsoCodeOrName" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"countryIsoCodeOrName": country_iso_code_or_name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetCountryByIsoCodeOrName", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_country_by_name(country_name: str) -> str:
        """Cove Data Protection Management Service method: GetCountryByName.

        JSON-RPC method: GetCountryByName

        Args:
            country_name: Required. Maps to "countryName" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"countryName": country_name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetCountryByName", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
