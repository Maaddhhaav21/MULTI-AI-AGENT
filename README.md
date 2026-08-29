# SIGNAL

### Intelligent Multi-Agent AI Console

> A modular AI agent application powered by **LangGraph, Groq, Tavily, and FastAPI**, with an interactive web interface for intelligent query processing and optional real-time web search.

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

The application is designed with a modular architecture so that additional models, tools, and agent capabilities can be integrated easily.

---

## ✨ Features

### 🤖 AI Agent

- LangGraph-based ReAct agent
- Configurable system prompt/persona
- Multiple supported LLM models
- Natural-language interaction
- Modular agent architecture

### 🔎 Real-Time Web Search

- Optional Tavily web-search integration
- Web search can be enabled or disabled per request
- Useful for queries requiring current or external information
- Search results can be incorporated into the agent's reasoning process

### ⚡ Fast LLM Inference

SIGNAL uses **Groq** for low-latency LLM inference.

Models available to the application depend on the models accessible through the configured Groq API account.

Example supported models:

```text
openai/gpt-oss-120b
openai/gpt-oss-20b
qwen/qwen3.8-27b