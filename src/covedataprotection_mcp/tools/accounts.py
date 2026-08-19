from collections.abc import Callable
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from .._json import dump_json_capped
from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN

_SCHEMA_HINT = "see Schema_23.3.json (linked in README) for exact field names"


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:
    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=False, idempotentHint=False))
    async def covedataprotection_add_account(
        account_info: Annotated[
            dict,
            Field(description=f"New account fields, per Cove's AccountInfo struct ({_SCHEMA_HINT})."),
        ],
        home_node_info: Annotated[
            dict,
            Field(
                description=f"Storage node to assign the account to, per Cove's HomeNodeInfo struct ({_SCHEMA_HINT})."
            ),
        ],
    ) -> str:
        """Create a new backup account (device) under a partner and storage node."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountInfo": account_info, "homeNodeInfo": home_node_info}
        try:
            result = await client.call("AddAccount", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True, idempotentHint=True))
    async def covedataprotection_enumerate_account_statistics(
        query: Annotated[
            dict,
            Field(
                description=f"Filter/selection criteria for the statistics query, per Cove's query struct ({_SCHEMA_HINT})."
            ),
        ],
    ) -> str:
        """List backup/usage statistics for accounts matching a query (data size, last backup, alerts)."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"query": query}
        try:
            result = await client.call("EnumerateAccountStatistics", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True, idempotentHint=True))
    async def covedataprotection_enumerate_accounts(
        partner_id: Annotated[int, Field(description="Partner ID whose backup accounts to list.")],
    ) -> str:
        """List backup accounts (devices) under a partner."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        try:
            result = await client.call("EnumerateAccounts", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True, idempotentHint=True))
    async def covedataprotection_get_account_features(
        account_id: Annotated[int, Field(description="Account ID to look up enabled features for.")],
    ) -> str:
        """Get which product features/modules are enabled for a backup account."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        try:
            result = await client.call("GetAccountFeatures", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True, idempotentHint=True))
    async def covedataprotection_get_account_info(
        name: Annotated[str, Field(description="Backup account's device login name.")],
        password: Annotated[str, Field(description="Backup account's device login password.")],
    ) -> str:
        """Look up a backup account by its own device login name and password."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"name": name, "password": password}
        try:
            result = await client.call("GetAccountInfo", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True, idempotentHint=True))
    async def covedataprotection_get_account_info_by_id(
        account_id: Annotated[int, Field(description="Account ID to fetch details for.")],
    ) -> str:
        """Get backup account details by numeric account ID."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        try:
            result = await client.call("GetAccountInfoById", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True))
    async def covedataprotection_modify_account(
        account_info: Annotated[
            dict,
            Field(
                description=f"Account fields to overwrite, per Cove's AccountInfo struct — must include the account's id ({_SCHEMA_HINT})."
            ),
        ],
        force_remove_custom_column_values_in_old_scope: Annotated[
            bool,
            Field(
                description="If moving the account to a new partner scope, whether to drop custom-column values that don't exist in the new scope."
            ),
        ],
    ) -> str:
        """Update a backup account's properties. Overwrites existing values; not reversible via this API."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {
            "accountInfo": account_info,
            "forceRemoveCustomColumnValuesInOldScope": force_remove_custom_column_values_in_old_scope,
        }
        try:
            result = await client.call("ModifyAccount", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True))
    async def covedataprotection_remove_account(
        account_id: Annotated[int, Field(description="ID of the backup account to permanently delete.")],
    ) -> str:
        """Permanently delete a backup account by ID. Irreversible; requires an explicit account ID."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        try:
            result = await client.call("RemoveAccount", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True))
    async def covedataprotection_set_account_features(
        account_id: Annotated[int, Field(description="Account ID to update feature flags for.")],
        features: Annotated[
            dict,
            Field(description=f"Feature flags to set, per Cove's features struct ({_SCHEMA_HINT})."),
        ],
    ) -> str:
        """Enable or disable specific product features on a backup account."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id, "features": features}
        try:
            result = await client.call("SetAccountFeatures", params)
            return dump_json_capped(result)
        except CoveError as e:
            return e.to_envelope()
