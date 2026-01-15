# Analyzer-GPT

An intelligent data analysis tool powered by multi-agent AI that automatically analyzes CSV data, generates insights, and creates visualizations using natural language queries.

## 🚀 Features

- **Natural Language Queries**: Ask questions about your data in plain English
- **Multi-Agent Architecture**: Uses AutoGen AgentChat with specialized agents for analysis and code execution
- **Safe Code Execution**: Runs Python code in isolated Docker containers
- **Interactive Web Interface**: Beautiful Streamlit-based UI for easy interaction
- **Automatic Visualization**: Generates plots and charts automatically
- **Error Handling**: Intelligent error recovery and debugging

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [License](#-license)

## 🏗️ Architecture

Analyzer-GPT uses a multi-agent system built on [AutoGen AgentChat](https://github.com/microsoft/autogen):

### Agents

1. **DataAnalyzerAgent**: 
   - Analyzes data and understands user queries
   - Generates Python code to answer questions
   - Provides insights and summaries

2. **CodeExecutorAgent**:
   - Executes Python code safely in Docker containers
   - Handles library installations
   - Returns execution results

### Team Structure

The agents work together using a `SelectorGroupChat` that intelligently routes tasks between agents based on the current context and requirements.

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Docker installed and running
- OpenAI API key

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Monish-Nallagondalla/Analyzer-GPT.git
   cd Analyzer-GPT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## ⚙️ Configuration

Configuration can be modified in `config/constants.py`:

- `MODEL`: OpenAI model to use (default: `gpt-4o`)
- `DOCKER_WORK_DIR`: Working directory for Docker execution (default: `temp`)
- `DOCKER_TIMEOUT`: Timeout for Docker operations in seconds (default: `120`)
- `MAX_TURNS`: Maximum conversation turns (default: `15`)
- `TEXT_MENTION_TERMINATION`: Termination keyword (default: `STOP`)

## 💻 Usage

### Web Interface (Recommended)

Launch the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Then:
1. Upload a CSV file through the web interface
2. Enter your question or task in natural language
3. View the analysis results and visualizations

### Command Line Interface

Run the main script:

```bash
python main.py
```

Modify the `task` variable in `main.py` to ask different questions about your data.

### Example Queries

- "Can you give me a graph of number of people who survived and died in the titanic Dataset?"
- "What is the average age of passengers?"
- "Show me the distribution of ticket prices"
- "Create a correlation matrix for numeric columns"

## 📁 Project Structure

```
Analyzer-GPT/
├── agents/
│   ├── code_executor_agent.py      # Code execution agent
│   ├── data_analyzer_agent.py      # Data analysis agent
│   └── prompts/
│       └── data_analyzer_prompt.py # Agent prompts
├── config/
│   ├── constants.py                 # Configuration constants
│   ├── docker_utils.py              # Docker executor utilities
│   └── model_client.py              # OpenAI model client
├── team/
│   └── analyzer_gpt_team.py         # Team configuration
├── temp/                            # Working directory (auto-generated)
├── main.py                          # CLI entry point
├── streamlit_app.py                 # Web interface
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 📦 Requirements

Key dependencies:

- `autogen-agentchat`: Multi-agent conversation framework
- `autogen-core`: Core AutoGen functionality
- `autogen-ext`: Extended AutoGen features including Docker support
- `streamlit`: Web interface framework
- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management

See `requirements.txt` for the complete list.

## 🔧 How It Works

1. **User Input**: User provides a CSV file and a natural language query
2. **Data Analysis**: DataAnalyzerAgent analyzes the query and generates Python code
3. **Code Execution**: CodeExecutorAgent executes the code in a Docker container
4. **Result Processing**: Results are analyzed and insights are generated
5. **Visualization**: If requested, plots are saved as `output.png`
6. **Output**: Final insights and visualizations are presented to the user

## 🐳 Docker

The project uses Docker containers for safe code execution. The default Docker image is `amancevice/pandas`, which includes pandas and other data science libraries.

Make sure Docker is running before using the application.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- Repository: [https://github.com/Monish-Nallagondalla/Analyzer-GPT](https://github.com/Monish-Nallagondalla/Analyzer-GPT)
- AutoGen Documentation: [https://microsoft.github.io/autogen/](https://microsoft.github.io/autogen/)

## ⚠️ Notes

- Ensure Docker is installed and running before use
- The application requires an active internet connection for OpenAI API calls
- Large datasets may take longer to process
- Generated files are stored in the `temp/` directory

---

Made with ❤️ using AutoGen AgentChat
