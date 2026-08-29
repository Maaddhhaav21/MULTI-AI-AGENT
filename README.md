# SIGNAL

### Intelligent Multi-Agent AI Console

> A modular AI agent application powered by LangGraph, Groq, Tavily, and FastAPI, with an interactive web interface for intelligent query processing and optional real-time web search.

---

## 🚀 Overview

**SIGNAL** is an AI-powered agent application designed to provide an interactive interface for working with Large Language Models and external tools.

The application combines:

- **LangGraph** for agent orchestration
- **Groq** for fast LLM inference
- **Tavily** for optional real-time web search
- **FastAPI** for the backend API
- **HTML, CSS, and JavaScript** for the interactive frontend

SIGNAL allows users to configure an AI agent's persona, select an available language model, submit queries, and optionally enable web search when up-to-date information is required.

The application follows a modular architecture, making it easier to extend with additional models, tools, and agent capabilities.

---

## ✨ Features

### 🤖 AI Agent

- ReAct-style AI agent powered by LangGraph
- Configurable system prompt and agent persona
- Support for multiple Groq-compatible models
- Natural-language interaction
- Modular agent architecture

### 🔎 Real-Time Web Search

- Optional web-search capability through Tavily
- Web search can be enabled or disabled for each request
- Useful for queries requiring current or external information
- Search results can be incorporated into the agent's response generation

### ⚡ Fast LLM Inference

SIGNAL uses **Groq** for fast LLM inference.

The application can be configured to use models available through the configured Groq API account.

Example models include:

```text
openai/gpt-oss-120b
openai/gpt-oss-20b
qwen/qwen3.8-27b
```

> Model availability depends on the models accessible through your Groq API account.

### 🌐 FastAPI Backend

SIGNAL exposes its agent through a REST API.

Main endpoint:

```http
POST /chat
```

Health endpoint:

```http
GET /health
```

FastAPI also provides interactive API documentation through Swagger UI.

### 🎨 SIGNAL Web Interface

The custom SIGNAL interface provides:

- AI model selection
- Agent persona configuration
- Query input
- Web-search toggle
- Agent pipeline visualization
- AI response display
- Response copying
- Backend connection status

---

# 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │      SIGNAL UI      │
                         │    Web Interface    │
                         └──────────┬──────────┘
                                    │
                                    │ HTTP
                                    ▼
                         ┌─────────────────────┐
                         │       FastAPI       │
                         │       Backend       │
                         └──────────┬──────────┘
                                    │
                                    │ /chat
                                    ▼
                         ┌─────────────────────┐
                         │      LangGraph      │
                         │     ReAct Agent     │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                         ▼                     ▼
                ┌─────────────────┐   ┌─────────────────┐
                │      Groq       │   │     Tavily      │
                │    LLM Model    │   │   Web Search    │
                └─────────────────┘   └─────────────────┘
```

---

# 🔄 Application Workflow

When a user submits a query, SIGNAL follows this workflow:

```text
User Query
    │
    ▼
SIGNAL Web Interface
    │
    ▼
POST /chat
    │
    ▼
FastAPI Request Validation
    │
    ▼
Model Validation
    │
    ▼
LangGraph ReAct Agent
    │
    ├────────────── Web Search Disabled ──────────────┐
    │                                                 │
    │                                                 ▼
    │                                               Groq
    │                                                 │
    │                                                 │
    └────────────── Web Search Enabled ──────────────┤
                                                      │
                                                      ▼
                                                   Tavily
                                                      │
                                                      ▼
                                                   Groq LLM
                                                      │
                                                      ▼
                                                Final Response
                                                      │
                                                      ▼
                                               SIGNAL Interface
```

---

# 📂 Project Structure

```text
MULTI-AI-AGENT/
│
├── app/
│   │
│   ├── __init__.py
│   │
│   ├── main.py
│   │
│   ├── backend/
│   │   ├── __init__.py
│   │   └── api.py
│   │
│   ├── core/
│   │   └── ai_agent.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── common/
│   │   ├── logger.py
│   │   └── custom_exception.py
│   │
│   └── frontend/
│       └── index.html
│
├── requirements.txt
├── setup.py
├── .env
├── .gitignore
└── README.md
```

---

# 📁 Component Responsibilities

| File / Directory | Responsibility |
|---|---|
| `app/main.py` | Application entry point and frontend serving |
| `app/backend/api.py` | FastAPI application and API endpoints |
| `app/core/ai_agent.py` | LangGraph agent and LLM/tool integration |
| `app/config/settings.py` | Environment variables and model configuration |
| `app/common/logger.py` | Application logging |
| `app/common/custom_exception.py` | Custom exception handling |
| `app/frontend/index.html` | SIGNAL web interface |
| `requirements.txt` | Python dependencies |
| `setup.py` | Python package configuration |
| `.env` | Local environment variables |

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **FastAPI** | Backend REST API |
| **Uvicorn** | ASGI server |
| **LangGraph** | Agent orchestration |
| **LangChain** | LLM and tool integrations |
| **Groq** | LLM inference |
| **Tavily** | Web search |
| **Pydantic** | Request validation |
| **python-dotenv** | Environment configuration |
| **HTML** | Frontend structure |
| **CSS** | Frontend styling |
| **JavaScript** | Frontend logic |
| **uv** | Python environment and dependency management |

---

# 🚀 Getting Started

## Prerequisites

Before running SIGNAL, make sure you have:

- Python 3.11+
- `uv`
- Groq API key
- Tavily API key

---

## 1. Clone the Repository

```bash
git clone https://github.com/Maaddhhaav21/MULTI-AI-AGENT.git

cd MULTI-AI-AGENT
```

---

## 2. Install Dependencies

Using `uv`:

```bash
uv sync
```

Alternatively, create a virtual environment and install the dependencies:

```bash
uv venv
```

Activate the environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Then install the dependencies:

```bash
uv pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

The application loads these credentials through environment variables.

### ⚠️ Security

Never commit your `.env` file to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# ▶️ Running SIGNAL

Start the application with:

```bash
uv run python -m app.main
```

The application runs locally at:

```text
http://127.0.0.1:9999
```

Open the URL in your browser to access the SIGNAL interface.

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Once the application is running, open:

```text
http://127.0.0.1:9999/docs
```

Swagger UI allows you to inspect and test the available API endpoints.

---

# 🔌 API Reference

## `POST /chat`

Processes a user query using the selected AI model.

### Request

```json
{
    "model_name": "openai/gpt-oss-120b",
    "system_prompt": "You are a helpful AI assistant.",
    "messages": [
        "Explain Retrieval-Augmented Generation."
    ],
    "allow_search": false
}
```

### Request Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `model_name` | `string` | Yes | LLM model used by the agent |
| `system_prompt` | `string` | Yes | Defines the agent's behavior and persona |
| `messages` | `string[]` | Yes | User query/messages |
| `allow_search` | `boolean` | Yes | Enables or disables Tavily web search |

### Example Response

```json
{
    "response": "Retrieval-Augmented Generation (RAG) is..."
}
```

---

# ❤️ Health Check

## `GET /health`

Returns the current application health status.

### Example Response

```json
{
    "status": "ok",
    "service": "MULTI AI AGENT"
}
```

---

# 🔎 Tavily Web Search

SIGNAL provides optional web-search functionality through Tavily.

When:

```json
"allow_search": true
```

the agent receives access to the Tavily search tool.

Example:

```json
{
    "model_name": "openai/gpt-oss-120b",
    "system_prompt": "You are a research assistant.",
    "messages": [
        "What are the latest developments in generative AI?"
    ],
    "allow_search": true
}
```

When web search is disabled:

```json
{
    "allow_search": false
}
```

the agent operates without the Tavily search tool.

---

# 🧠 Agent Architecture

SIGNAL uses a **ReAct-style agent workflow** through LangGraph.

ReAct combines reasoning and tool usage, allowing the agent to determine when external information may be useful.

Conceptually:

```text
                   User Query
                       │
                       ▼
                ┌──────────────┐
                │   AI Agent   │
                └──────┬───────┘
                       │
                       ▼
                  Reasoning
                       │
              ┌────────┴────────┐
              │                 │
        Need Search?          No Search
              │                 │
             YES                │
              │                 │
              ▼                 │
       Tavily Web Search        │
              │                 │
              ▼                 │
        Search Results          │
              │                 │
              └────────┬────────┘
                       │
                       ▼
                   Groq LLM
                       │
                       ▼
                Final Response
```

---

# 🤖 Supported Models

Model availability depends on the models accessible through the configured Groq API account.

The application can be configured with models such as:

```text
openai/gpt-oss-120b
openai/gpt-oss-20b
qwen/qwen3.8-27b
```

Models are controlled through:

```text
app/config/settings.py
```

Example:

```python
ALLOWED_MODEL_NAMES = [
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "qwen/qwen3.8-27b"
]
```

> The available model names may change depending on your Groq account and the models currently provided by Groq.

---

# ⚙️ Configuration

Application configuration is managed through:

```text
app/config/settings.py
```

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES = [
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b",
        "qwen/qwen3.8-27b"
    ]


settings = Settings()
```

---

# 🧪 Testing

## Test the Backend

Check whether the backend is running:

```bash
curl http://127.0.0.1:9999/health
```

Expected response:

```json
{
    "status": "ok",
    "service": "MULTI AI AGENT"
}
```

---

## Test the AI Agent

```bash
curl -X POST http://127.0.0.1:9999/chat \
-H "Content-Type: application/json" \
-d '{
    "model_name": "openai/gpt-oss-120b",
    "system_prompt": "You are a helpful AI assistant.",
    "messages": [
        "Explain AI agents in simple terms."
    ],
    "allow_search": false
}'
```

---

## Test Web Search

```bash
curl -X POST http://127.0.0.1:9999/chat \
-H "Content-Type: application/json" \
-d '{
    "model_name": "openai/gpt-oss-120b",
    "system_prompt": "You are a research assistant.",
    "messages": [
        "What are the latest developments in AI agents?"
    ],
    "allow_search": true
}'
```

---

# 🛡️ Error Handling

SIGNAL uses FastAPI HTTP exceptions together with custom exception handling.

The API validates:

- Request structure
- Model availability
- Agent execution
- External API failures

Invalid model requests return an HTTP `400` response.

Agent execution failures return an HTTP `500` response.

Application events and errors are logged using the project's logging utilities.

---

# 🔒 Security

SIGNAL follows basic security practices:

- API keys are stored in environment variables.
- `.env` is excluded from version control.
- Pydantic validates incoming API requests.
- Model selection is restricted using an allowlist.
- Web search is explicitly controlled per request.
- API credentials are not exposed to the frontend.

### Never expose API keys

❌ Do not hard-code credentials:

```python
GROQ_API_KEY = "gsk_xxxxxxxxx"
```

✅ Use environment variables:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 🚢 Deployment

SIGNAL can be deployed to cloud platforms that support Python and FastAPI applications.

Possible deployment platforms include:

- Vercel
- Railway
- Render
- Other Python-compatible hosting platforms

For production deployment, configure the following environment variables:

```text
GROQ_API_KEY
TAVILY_API_KEY
```

Do not commit these credentials to source control.

For cloud environments, the application should listen on:

```text
0.0.0.0
```

and use the port provided by the hosting platform.

---

# 📦 Production Architecture

A production deployment can follow this architecture:

```text
                     Internet
                         │
                         ▼
                ┌─────────────────┐
                │     SIGNAL      │
                │   Web Frontend  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     FastAPI     │
                │      API        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    LangGraph    │
                │   ReAct Agent   │
                └────────┬────────┘
                         │
                 ┌───────┴────────┐
                 │                │
                 ▼                ▼
              Groq             Tavily
              LLM              Search
                 │                │
                 └───────┬────────┘
                         ▼
                    AI Response
```

---

# 📊 Project Highlights

SIGNAL demonstrates practical implementation of several modern AI engineering concepts.

### LLM Integration

Integration of external LLM inference through Groq.

### Agentic AI

Implementation of a ReAct-style agent using LangGraph.

### Tool Calling

Integration of Tavily as an external web-search tool.

### API Development

REST API implementation using FastAPI.

### Request Validation

Structured request validation using Pydantic.

### Environment Configuration

Secure configuration through environment variables.

### Modular Architecture

Separation of:

- API layer
- Agent layer
- Configuration
- Common utilities
- Frontend

### Frontend Integration

A custom web interface communicates with the FastAPI backend and displays generated agent responses.

---

# 🎯 Use Cases

SIGNAL can be used for a variety of AI-assisted tasks, including:

- General question answering
- AI research assistance
- Technical explanations
- Current-event research
- Information retrieval
- AI/ML learning assistance
- Web-assisted question answering
- Experimentation with agentic AI workflows

---

# 🔮 Future Improvements

Potential future enhancements include:

- [ ] Conversation memory
- [ ] Persistent chat history
- [ ] Streaming LLM responses
- [ ] Multi-agent collaboration
- [ ] Additional external tools
- [ ] Support for additional LLM providers
- [ ] Authentication and authorization
- [ ] User-specific sessions
- [ ] Agent observability and tracing
- [ ] Automated response evaluation
- [ ] Unit and integration testing
- [ ] Rate limiting
- [ ] Production monitoring
- [ ] Docker support
- [ ] Improved response formatting

---

# 💡 Why SIGNAL?

SIGNAL was built to explore the practical implementation of **agentic AI systems** rather than simply creating a basic LLM API wrapper.

The project combines:

```text
LLM
+
Agent Orchestration
+
ReAct Reasoning
+
Tool Calling
+
Web Search
+
REST API
+
Interactive UI
```

into a single AI application.

The modular architecture makes it possible to introduce additional models, tools, and capabilities without fundamentally changing the application's interface.

---

# 👨‍💻 Author

## Madhav Manoj


---


<p align="center">

### SIGNAL

**Intelligent Multi-Agent AI Console**

Built with Python • FastAPI • LangGraph • Groq • Tavily

</p>