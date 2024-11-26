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

You can install **Agent Watch** via [PyPI](https://pypi.org/project/agent-watch/) using `pip`:

```bash
pip install agent-watch
```

## Usage

### Basic Example

Here's a simple example of how to use **Agent Watch** to monitor a Crew AI workflow:

```python
from agent_watch import AgentWatchExtended

# Initialize Agent Watch
rag_watch = AgentWatchExtended(model="gpt-4o")

# Start monitoring
rag_watch.start()

# Your Crew AI operations go here
# For example:
# output = your_crew_ai_function()

# Set token counts (replace with actual values)
input_text = "Your input text here."
output_text = "Your output text here."
rag_watch.set_token_counts(input_text=input_text, output_text=output_text)

# End monitoring
rag_watch.end()

# Visualize the results
rag_watch.visualize(method='cli')  # For CLI summary
```

### Integration with Crew AI

Integrate **Agent Watch** with a Crew AI application to monitor operational metrics effectively.

#### `app.py`

```python
# app.py

from agent_watch import AgentWatchExtended
from crewai_tools import ScrapeWebsiteTool, FileWriterTool, TXTSearchTool
from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Initialize Agent Watch
rag_watch = AgentWatchExtended(model="gpt-4o")  # Specify the model being used

# Start monitoring
rag_watch.start()

# Initialize the ScrapeWebsiteTool
scrape_tool = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Artificial_intelligence')  

# Extract the text
text = scrape_tool.run()
print("Scraped Text:", text[:500], "...")  # Print first 500 characters for brevity

# Initialize the FileWriterTool
file_writer_tool = FileWriterTool()
text_cleaned = text.encode("ascii", "ignore").decode()
# Write content to a file in a specified directory
write_result = file_writer_tool._run(filename='ai.txt', content=text_cleaned, overwrite="True")
print("File Write Result:", write_result)

# Initialize the TXTSearchTool
txt_search_tool = TXTSearchTool(txt='ai.txt')
context = txt_search_tool.run('What is natural language processing?')
print("Context for NLP:", context)

# Create the Agent
data_analyst = Agent(
    role='Educator',
    goal=f'Based on the context provided, answer the question - What is Natural Language Processing? Context - {context}',
    backstory='You are a data expert',
    verbose=True,
    allow_delegation=False,
    tools=[txt_search_tool]
)

# Create the Task
test_task = Task(
    description="Understand the topic and give the correct response",
    tools=[txt_search_tool],
    agent=data_analyst,
    expected_output='Provide a correct response about Natural Language Processing.'
)

# Create the Crew
crew = Crew(
    agents=[data_analyst],
    tasks=[test_task]
)

# Kickoff the Crew
output = crew.kickoff()
print("Crew Output:", output)

# Set token counts using CrewOutput
rag_watch.set_token_usage_from_crew_output(output)

# End monitoring
rag_watch.end()

# Optionally, visualize the results
rag_watch.visualize(method='cli')  # For CLI summary
```

## API Reference

### AgentWatch

The `AgentWatch` class is the core component responsible for monitoring and logging operational metrics.

#### Initialization

```python
AgentWatch(model: str, enable_monitoring: bool = True)
```

- **Parameters**:
  - `model` (str): The model name (e.g., `"gpt-4o"`).
  - `enable_monitoring` (bool, optional): Flag to enable or disable resource monitoring. Defaults to `True`.

#### Methods

- `start()`: Starts monitoring resources and logging.
- `end()`: Stops monitoring, calculates metrics, and logs the results.
- `set_token_counts(input_text: str, output_text: str)`: Sets the token counts based on input and output texts.
- `set_token_usage_from_crew_output(crew_output)`: Extracts token usage from a `CrewOutput` object.
- `set_carbon_emissions_resource_based(avg_cpu_usage: float, avg_memory_usage: float, emission_factor: float = 0.453)`: Calculates CO2 emissions based on resource usage.
- `count_tokens(text: str) -> int`: Counts the number of tokens in a given text.

### AgentWatchExtended

The `AgentWatchExtended` class extends `AgentWatch` by adding visualization capabilities.

#### Initialization

```python
AgentWatchExtended(model: str, enable_monitoring: bool = True)
```

- **Parameters**:
  - `model` (str): The model name (e.g., `"gpt-4o"`).
  - `enable_monitoring` (bool, optional): Flag to enable or disable resource monitoring. Defaults to `True`.

#### Methods

- Inherits all methods from `AgentWatch`.
- `visualize(method='cli')`: Visualizes the collected metrics.
  - **Parameters**:
    - `method` (str): The visualization method, either `'cli'` or `'streamlit'`.

## Logging

**Agent Watch** uses a logging mechanism to record all operations and metrics.

- **Log File**: `agent_watch.log`
- **Log Contents**:
  - Monitoring start and end times
  - Token counts
  - Costs
  - CPU and memory usage
  - Carbon emissions

**Logger Class**: Responsible for writing logs to both the console and the log file.

## Visualization

**Agent Watch** provides visualization tools to display the collected metrics.

### CLI Summary

Prints a summary of all metrics directly to the console.

```python
rag_watch.visualize(method='cli')
```

### Streamlit Dashboard

Launches a web-based dashboard displaying detailed metrics and graphs.

#### Creating a Streamlit Script

Create a separate script, e.g., `visualize.py`:

```python
# visualize.py

from agent_watch import AgentWatchExtended

# Initialize Agent Watch with the same model
rag_watch = AgentWatchExtended(model="gpt-4o")

# Set token counts and other metrics manually or load from logs
# For demonstration, we'll use dummy data
input_text = "Example input text."
output_text = "Example output text generated by the AI."

rag_watch.set_token_counts(input_text=input_text, output_text=output_text)
rag_watch.end()

# Launch Streamlit dashboard
rag_watch.visualize(method='streamlit')
```

#### Running the Streamlit App

Execute the following command to launch the dashboard:

```bash
streamlit run visualize.py
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**

    ```bash
    git checkout -b feature/YourFeature
    ```

3. **Commit Your Changes**

    ```bash
    git commit -m "Add Your Feature"
    ```

4. **Push to the Branch**

    ```bash
    git push origin feature/YourFeature
    ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

**Your Name**  
Email: [sonu@aianytime.net](mailto:sonu@aianytime.net)
