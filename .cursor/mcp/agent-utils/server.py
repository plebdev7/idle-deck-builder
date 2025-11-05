#!/usr/bin/env python3
"""Agent utilities MCP server."""

import asyncio
from datetime import datetime
from typing import Optional
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio


# Create server instance
server = Server("agent-utils")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="get_timestamp",
            description="Get the current timestamp in specified format. "
                       "Supports multiple formats and timezone options.",
            inputSchema={
                "type": "object",
                "properties": {
                    "format": {
                        "type": "string",
                        "description": "Format string: 'default' for 'YYYY-MM-DD HH:MM:SS', "
                                     "'iso' for ISO 8601, or custom strftime format (e.g., '%Y-%m-%d')",
                        "default": "default"
                    },
                    "timezone": {
                        "type": "string",
                        "description": "Timezone: 'local' for system local time, 'utc' for UTC",
                        "enum": ["local", "utc"],
                        "default": "local"
                    }
                },
            },
        ),
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle tool execution requests."""
    
    if name != "get_timestamp":
        raise ValueError(f"Unknown tool: {name}")
    
    # Extract parameters with defaults
    format_str = arguments.get("format", "default") if arguments else "default"
    timezone_str = arguments.get("timezone", "local") if arguments else "local"
    
    try:
        # Get current time based on timezone
        if timezone_str == "utc":
            from datetime import timezone as tz
            now = datetime.now(tz.utc)
        else:
            now = datetime.now()
        
        # Format timestamp
        if format_str == "default":
            # Default format: YYYY-MM-DD HH:MM:SS
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        elif format_str == "iso":
            # ISO 8601 format with timezone
            timestamp = now.isoformat()
        else:
            # Custom strftime format
            timestamp = now.strftime(format_str)
        
        return [types.TextContent(type="text", text=timestamp)]
    
    except Exception as e:
        return [types.TextContent(type="text", text=f"Error generating timestamp: {str(e)}")]


async def main():
    """Main entry point for the server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="agent-utils",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())


