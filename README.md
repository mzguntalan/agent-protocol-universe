# Agent Protocol Universe (APU)

**Streamline MCP Tool Integration for AI Agents**

[![GitHub Stars](https://img.shields.io/github/stars/mzguntalan/agent-protocol-universe?style=social)](https://github.com/mzguntalan/agent-protocol-universe/stargazers)
[![License](https://img.shields.io/github/license/mzguntalan/agent-protocol-universe)](LICENSE)

**APU** is a centralized library designed to simplify the integration of verified Model Context Protocol (MCP) tools into AI agents. By reducing manual configuration and automating setup processes, APU enables developers to build and deploy multi-tool agents more efficiently.

---

## What is MCP?

The **Model Context Protocol (MCP)** is an open standard that standardizes how applications provide context to large language models (LLMs). Think of MCP as the "USB-C port" for AI applications, offering a universal interface to connect AI models with various data sources and tools. This protocol allows AI agents to access and interact with external applications like Blender, VS Code, and more ([docs.anthropic.com](https://docs.anthropic.com/en/docs/agents-and-tools/mcp?utm_source=chatgpt.com)).

---

## Key Features

* **Centralized Access to Verified MCP Tools**:
  
  * Easily discover, query, and call a wide array of verified MCP tools.

  ```python
  tool = apu.find("render scene")  # Search across all tools
  tool = apu.vscode.find("lint Python file")  # Search within VS Code tools
  ```

* **Dynamic Toolbox Management**:
  
  * Developers can enable or disable specific tools within the agent's toolbox.

* **Automated Setup and Configuration**:

  * Detects missing plugins or application dependencies.
  * Automatically installs required applications and configures them for MCP compatibility.
  * Modifies configuration files as needed to ensure seamless integration.

  ```python
  apu.start("vscode", "blender")  # Initialize and configure tools
  ```

* **Quick Agent Setup**:
  * Streamlines agent development workflows by abstracting low-level setup details.

---

## Installation

To install APU, use pip (coming soon!):

```bash
pip install apu
```

Please make sure that you have the necessary permissions to install applications and modify configurations on your system.

---

## Configuration

After installation, you can configure APU using the following helper functions:

```python
import apu

apu.list_available()     # List all available MCP tools
apu.check_env()          # Check the current environment for tool compatibility
apu.auto_install()       # Automatically install and configure required tools
apu.custom_tools()       # Integrate custom, non-verified MCP tools
```

Note: The `custom_tools()` function allows developers to include their own MCP tools, though this process may be more complex and require additional configuration.

---

## Collection of MCPs




---

## Contributing

We welcome contributions from the community! To contribute, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) for more detailed guidelines.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Roadmap

* [ ] Expand the library of verified MCP tools.
* [ ] Support for custom tool integration.
* [ ] Improve documentation and usage examples.
* [ ] Develop a CLI/GUI for easier tool management.

---

<!--## Community

Join our community to stay updated and collaborate:

* [GitHub Discussions](https://github.com/mzguntalan/agent-protocol-universe/discussions)

We encourage open discussions, feedback, and collaboration to improve APU.-->
