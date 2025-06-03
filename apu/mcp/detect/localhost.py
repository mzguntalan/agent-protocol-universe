"""Detect MCP servers running on localhost"""

from typing import Any
from typing import List

McpServer = Any


def list_configured_servers() -> List[McpServer]: ...


def list_running_servers() -> List[McpServer]: ...


def list_available_to_query_servers() -> List[McpServer]: ...
