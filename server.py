from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "server",
    host="0.0.0.0",   # listen on all network interfaces
    port=8000,        # stay on the same port
)

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
