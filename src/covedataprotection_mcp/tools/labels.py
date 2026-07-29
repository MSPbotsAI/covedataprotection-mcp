import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_account_label(account_id_collection: list[int], label_collection: list[str]) -> str:
        """Cove Data Protection Management Service method: AddAccountLabel.

        JSON-RPC method: AddAccountLabel

        Args:
            account_id_collection: Required. Maps to "accountIdCollection" (list[int]).
            label_collection: Required. Maps to "labelCollection" (list[str]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountIdCollection": account_id_collection, "labelCollection": label_collection}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddAccountLabel", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_add_labels(account_id: int, label_collection: list[str]) -> str:
        """Cove Data Protection Management Service method: AddLabels.

        JSON-RPC method: AddLabels

        Args:
            account_id: Required. Maps to "accountId" (int).
            label_collection: Required. Maps to "labelCollection" (list[str]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id, "labelCollection": label_collection}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddLabels", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_ids_by_label(label: str) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountIdsByLabel.

        JSON-RPC method: EnumerateAccountIdsByLabel

        Args:
            label: Required. Maps to "label" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"label": label}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountIdsByLabel", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_labels_by_account_id(account_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountLabelsByAccountId.

        JSON-RPC method: EnumerateAccountLabelsByAccountId

        Args:
            account_id: Required. Maps to "accountId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountLabelsByAccountId", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_labels_by_account_ids(account_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountLabelsByAccountIds.

        JSON-RPC method: EnumerateAccountLabelsByAccountIds

        Args:
            account_ids: Required. Maps to "accountIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountIds": account_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountLabelsByAccountIds", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_account_labels_by_names(label_collection: list[str]) -> str:
        """Cove Data Protection Management Service method: EnumerateAccountLabelsByNames.

        JSON-RPC method: EnumerateAccountLabelsByNames

        Args:
            label_collection: Required. Maps to "labelCollection" (list[str]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"labelCollection": label_collection}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAccountLabelsByNames", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_all_labels() -> str:
        """Cove Data Protection Management Service method: EnumerateAllLabels.

        JSON-RPC method: EnumerateAllLabels

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAllLabels", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_account_label(account_id_collection: list[int], label_collection: list[str]) -> str:
        """Cove Data Protection Management Service method: RemoveAccountLabel.

        JSON-RPC method: RemoveAccountLabel

        Args:
            account_id_collection: Required. Maps to "accountIdCollection" (list[int]).
            label_collection: Required. Maps to "labelCollection" (list[str]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountIdCollection": account_id_collection, "labelCollection": label_collection}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveAccountLabel", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_labels(account_id: int, label_collection: list[str]) -> str:
        """Cove Data Protection Management Service method: RemoveLabels.

        JSON-RPC method: RemoveLabels

        Args:
            account_id: Required. Maps to "accountId" (int).
            label_collection: Required. Maps to "labelCollection" (list[str]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"accountId": account_id, "labelCollection": label_collection}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveLabels", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
