import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_product(product_info: dict) -> str:
        """Cove Data Protection Management Service method: AddProduct.

        JSON-RPC method: AddProduct

        Args:
            product_info: Required. Maps to "productInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"productInfo": product_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddProduct", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_products(partner_id: int, current_partner_only: bool) -> str:
        """Cove Data Protection Management Service method: EnumerateProducts.

        JSON-RPC method: EnumerateProducts

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            current_partner_only: Required. Maps to "currentPartnerOnly" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "currentPartnerOnly": current_partner_only}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateProducts", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_find_product_by_name(partner_id: int, name: str) -> str:
        """Cove Data Protection Management Service method: FindProductByName.

        JSON-RPC method: FindProductByName

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            name: Required. Maps to "name" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "name": name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("FindProductByName", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_product_info(product_id: int, return_modified_features_only: bool) -> str:
        """Cove Data Protection Management Service method: GetProductInfo.

        JSON-RPC method: GetProductInfo

        Args:
            product_id: Required. Maps to "productId" (int).
            return_modified_features_only: Required. Maps to "returnModifiedFeaturesOnly" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"productId": product_id, "returnModifiedFeaturesOnly": return_modified_features_only}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetProductInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_product_info_with_extra_features(product_id: int, return_modified_features_only: bool) -> str:
        """Cove Data Protection Management Service method: GetProductInfoWithExtraFeatures.

        JSON-RPC method: GetProductInfoWithExtraFeatures

        Args:
            product_id: Required. Maps to "productId" (int).
            return_modified_features_only: Required. Maps to "returnModifiedFeaturesOnly" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"productId": product_id, "returnModifiedFeaturesOnly": return_modified_features_only}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetProductInfoWithExtraFeatures", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_product(product_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyProduct.

        JSON-RPC method: ModifyProduct

        Args:
            product_info: Required. Maps to "productInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"productInfo": product_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyProduct", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_product(product_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveProduct.

        JSON-RPC method: RemoveProduct

        Args:
            product_id: Required. Maps to "productId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"productId": product_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveProduct", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
