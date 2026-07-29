import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_contact_note(contact_note_info: dict) -> str:
        """Cove Data Protection Management Service method: AddContactNote.

        JSON-RPC method: AddContactNote

        Args:
            contact_note_info: Required. Maps to "contactNoteInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactNoteInfo": contact_note_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddContactNote", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_add_contact_person(contact_person_info: dict) -> str:
        """Cove Data Protection Management Service method: AddContactPerson.

        JSON-RPC method: AddContactPerson

        Args:
            contact_person_info: Required. Maps to "contactPersonInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactPersonInfo": contact_person_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddContactPerson", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_all_contact_persons(root_partner_id: int, contact_person_types: list[str], apply_mailing_option: bool) -> str:
        """Cove Data Protection Management Service method: EnumerateAllContactPersons.

        JSON-RPC method: EnumerateAllContactPersons

        Args:
            root_partner_id: Required. Maps to "rootPartnerId" (int).
            contact_person_types: Required. Maps to "contactPersonTypes" (list[str]).
            apply_mailing_option: Required. Maps to "applyMailingOption" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"rootPartnerId": root_partner_id, "contactPersonTypes": contact_person_types, "applyMailingOption": apply_mailing_option}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateAllContactPersons", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_contact_notes(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateContactNotes.

        JSON-RPC method: EnumerateContactNotes

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateContactNotes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_contact_persons(partner_ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateContactPersons.

        JSON-RPC method: EnumerateContactPersons

        Args:
            partner_ids: Required. Maps to "partnerIds" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerIds": partner_ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateContactPersons", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_last_contact_notes(partners: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateLastContactNotes.

        JSON-RPC method: EnumerateLastContactNotes

        Args:
            partners: Required. Maps to "partners" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partners": partners}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateLastContactNotes", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_contact_note_info(contact_note_id: int) -> str:
        """Cove Data Protection Management Service method: GetContactNoteInfo.

        JSON-RPC method: GetContactNoteInfo

        Args:
            contact_note_id: Required. Maps to "contactNoteId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactNoteId": contact_note_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetContactNoteInfo", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_contact_person_info_by_id(contact_person_id: int) -> str:
        """Cove Data Protection Management Service method: GetContactPersonInfoById.

        JSON-RPC method: GetContactPersonInfoById

        Args:
            contact_person_id: Required. Maps to "contactPersonId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactPersonId": contact_person_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetContactPersonInfoById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_contact_note(contact_note_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyContactNote.

        JSON-RPC method: ModifyContactNote

        Args:
            contact_note_info: Required. Maps to "contactNoteInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactNoteInfo": contact_note_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyContactNote", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_modify_contact_person(contact_person_info: dict) -> str:
        """Cove Data Protection Management Service method: ModifyContactPerson.

        JSON-RPC method: ModifyContactPerson

        Args:
            contact_person_info: Required. Maps to "contactPersonInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactPersonInfo": contact_person_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ModifyContactPerson", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_contact_note(contact_note_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveContactNote.

        JSON-RPC method: RemoveContactNote

        Args:
            contact_note_id: Required. Maps to "contactNoteId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactNoteId": contact_note_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveContactNote", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_remove_contact_person(contact_person_id: int) -> str:
        """Cove Data Protection Management Service method: RemoveContactPerson.

        JSON-RPC method: RemoveContactPerson

        Args:
            contact_person_id: Required. Maps to "contactPersonId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"contactPersonId": contact_person_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("RemoveContactPerson", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
