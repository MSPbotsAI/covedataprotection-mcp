import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import CoveClient, CoveError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], CoveClient | None]) -> None:

    @mcp.tool()
    async def covedataprotection_add_root_job(partner_id: int, specification: dict, executor_id: int) -> str:
        """Cove Data Protection Management Service method: AddRootJob.

        JSON-RPC method: AddRootJob

        Args:
            partner_id: Required. Maps to "partnerId" (int).
            specification: Required. Maps to "specification" (dict).
            executor_id: Required. Maps to "executorId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id, "specification": specification, "executorId": executor_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("AddRootJob", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_control_job(job_id: int, action: str) -> str:
        """Cove Data Protection Management Service method: ControlJob.

        JSON-RPC method: ControlJob

        Args:
            job_id: Required. Maps to "jobId" (int).
            action: Required. Maps to "action" (str).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"jobId": job_id, "action": action}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ControlJob", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_jobs(partner_id: int) -> str:
        """Cove Data Protection Management Service method: EnumerateJobs.

        JSON-RPC method: EnumerateJobs

        Args:
            partner_id: Required. Maps to "partnerId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"partnerId": partner_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateJobs", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_jobs_by_ids(ids: list[int]) -> str:
        """Cove Data Protection Management Service method: EnumerateJobsByIds.

        JSON-RPC method: EnumerateJobsByIds

        Args:
            ids: Required. Maps to "ids" (list[int]).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"ids": ids}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateJobsByIds", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_enumerate_jobs_by_parent_id(parent_job_id: int, fetch_recursively: bool) -> str:
        """Cove Data Protection Management Service method: EnumerateJobsByParentId.

        JSON-RPC method: EnumerateJobsByParentId

        Args:
            parent_job_id: Required. Maps to "parentJobId" (int).
            fetch_recursively: Required. Maps to "fetchRecursively" (bool).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"parentJobId": parent_job_id, "fetchRecursively": fetch_recursively}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("EnumerateJobsByParentId", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_finish_job_execution(job_id: int, execution_info: dict) -> str:
        """Cove Data Protection Management Service method: FinishJobExecution.

        JSON-RPC method: FinishJobExecution

        Args:
            job_id: Required. Maps to "jobId" (int).
            execution_info: Required. Maps to "executionInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"jobId": job_id, "executionInfo": execution_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("FinishJobExecution", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_get_job_by_id(job_id: int) -> str:
        """Cove Data Protection Management Service method: GetJobById.

        JSON-RPC method: GetJobById

        Args:
            job_id: Required. Maps to "jobId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"jobId": job_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("GetJobById", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_report_job_execution_progress(job_id: int, execution_info: dict) -> str:
        """Cove Data Protection Management Service method: ReportJobExecutionProgress.

        JSON-RPC method: ReportJobExecutionProgress

        Args:
            job_id: Required. Maps to "jobId" (int).
            execution_info: Required. Maps to "executionInfo" (dict).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"jobId": job_id, "executionInfo": execution_info}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("ReportJobExecutionProgress", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def covedataprotection_take_job_for_execution(executor_type: str, executor_id: int) -> str:
        """Cove Data Protection Management Service method: TakeJobForExecution.

        JSON-RPC method: TakeJobForExecution

        Args:
            executor_type: Required. Maps to "executorType" (str).
            executor_id: Required. Maps to "executorId" (int).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"executorType": executor_type, "executorId": executor_id}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            result = await client.call("TakeJobForExecution", params)
            return json.dumps(result, indent=2, default=str)
        except CoveError as e:
            return f"Error: {e}"
