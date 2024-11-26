# Agent Watch

**Agent Watch** is an operational monitoring library for Crew AI applications. It captures essential metrics such as token counts, costs, execution time, resource utilization, carbon emissions, and detailed logs. Additionally, it offers both textual and visual representations of the collected data via a Command-Line Interface (CLI) or a Streamlit dashboard.

## Features

1. **Token Counting**
   - Total tokens
   - Input tokens
   - Output tokens

2. **Cost Calculation**
   - Based on the token usage and model pricing

3. **Performance Metrics**
   - Time taken for each call
   - CPU and memory consumption

4. **Environmental Impact**
   - Estimated CO₂ emissions

5. **Logging**
   - Comprehensive logs of all operations

6. **Visualization**
   - CLI summaries
   - Streamlit dashboard for detailed insights

## Installation

You can install **Agent Watch** via `pip`. If not published to PyPI, install it locally:

```bash
pip install .
