# Agent Utilities MCP Server

A Model Context Protocol (MCP) server providing utility tools for AI agents.

## Features

- **Timestamp Tool**: Get current timestamp in various formats
  - ISO 8601 format (default)
  - Custom strftime formats
  - Local or UTC timezone support

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure in `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "agent-utils": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "${workspaceFolder}/.cursor/mcp/agent-utils",
      "env": {}
    }
  }
}
```

## Available Tools

### get_timestamp

Get the current timestamp in specified format.

**Parameters:**
- `format` (optional): Format string - "iso" for ISO 8601 (default), or custom strftime format
- `timezone` (optional): "local" (default) or "utc"

**Returns:** String containing the formatted timestamp

**Examples:**
- ISO 8601 local time: `get_timestamp()`
- ISO 8601 UTC: `get_timestamp(timezone="utc")`
- Custom format: `get_timestamp(format="%Y-%m-%d %H:%M:%S")`

## Usage

The server runs automatically when configured in Cursor. Tools will be available in the Composer Agent.


