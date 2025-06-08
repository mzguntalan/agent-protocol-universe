from typing import List

def start(*servers: str) -> None:
    """
    Initialize, validate, configure and start up the external application for the MCP servers.
    """
    _check_env()
    _auto_install()
    pass
    
def find(query: str, top_k = int):
    """
    Find the best top K tools from the choosen MCP servers, based on the query.
    For now, the query will be the tool name, later, it should be the query from user or agent.
    Then the query will be passed as the input to the LLM or embedding.
    """
    pass
    
def _check_env():
    pass

def _auto_install():
    """
    Under start function or auto_setup(), auto_config()
    """
    pass
    
def custom_tools() :
    """
    Let developers include their own non-verified MCP tools. Gonna be complicated.
    """
    pass
    
   
    
    
    