# Agent Watch

![PyPI](https://img.shields.io/pypi/v/agent-watch)
![License](https://img.shields.io/pypi/l/agent-watch)
![Python Version](https://img.shields.io/pypi/pyversions/agent-watch)

**Agent Watch** is an AI AgentOps monitoring library designed for Crew AI applications. It captures essential metrics such as token counts, costs, execution time, resource utilization, and carbon emissions. Additionally, it offers comprehensive logging and visualization tools, enabling both textual and graphical representations of the collected data via a Command-Line Interface (CLI) or a Streamlit dashboard.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Example](#basic-example)
  - [Integration with Crew AI](#integration-with-crew-ai)
- [API Reference](#api-reference)
  - [AgentWatch](#agentwatch)
  - [AgentWatchExtended](#agentwatchextended)
- [Logging](#logging)
- [Visualization](#visualization)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

1. **Token Counting**
   - Total tokens
   - Input tokens
   - Output tokens

2. **Cost Calculation**
   - Based on token usage and model pricing

3. **Performance Metrics**
   - Execution time
   - CPU and memory consumption

4. **Environmental Impact**
   - Estimated CO₂ emissions based on resource usage

5. **Logging**
   - Comprehensive logs of all operations

6. **Visualization**
   - CLI summaries
   - Streamlit dashboard for detailed insights
