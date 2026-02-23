# 🔧 Manual Tool Router Agent

> A lightweight AI agent demonstrating **manual tool routing & function calling theory** — powered by Groq LLM and Streamlit.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=flat-square)](https://groq.com)

---

## 📖 Overview

This project implements a simplified **agent architecture from scratch** — without relying on automatic function-calling APIs. It's designed to teach you how real AI agents reason, select tools, and produce answers.

```
User Goal → Reason → Select Tool → Execute Tool → Reason → Final Answer
```

Whether you're building ReAct agents, multi-step planners, or autonomous systems, this project gives you the conceptual and practical foundation.

---

## 🚀 Live Demo

> 👉 **[Launch App](https://manual-tool-router-agent.streamlit.app/)** _(replace with your deployed URL)_

---

## 🧠 What You'll Learn

| Concept | Description |
|---|---|
| **Tool Abstraction** | How to define and expose tools to an LLM |
| **Manual Function Calling** | Route tool calls without relying on API magic |
| **LLM-Driven Tool Selection** | Let the model decide when and which tool to use |
| **Deterministic Execution** | Safely execute selected tools with predictable output |
| **Two-Pass Reasoning** | First pass selects tools; second pass synthesizes the final answer |

This is the foundation for:
- ⚛️ ReAct agents
- 🗺️ Multi-step planners
- 🤖 Autonomous agents
- 🔌 Tool-augmented LLM systems

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│             User Goal               │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│     LLM Pass 1: Tool Selection      │
│   "Should I use a tool, and which?" │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│         Manual Tool Router          │
│   Routes to the appropriate tool    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│        Tool Execution Layer         │
│   Calculator · Web Search · etc.    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│     LLM Pass 2: Final Reasoning     │
│   Synthesizes tool output + answer  │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│            Final Answer             │
└─────────────────────────────────────┘
```

---

## 📁 Project Structure

```
Manual-Tool-Router-Agent/
│
├── app.py              # Streamlit UI — the user-facing interface
├── agent.py            # Core agent logic — reasoning & routing
├── tools.py            # Tool definitions — calculator, search, etc.
├── requirements.txt    # Python dependencies
├── .env                # Local secrets (not committed)
└── README.md
```

---

## 🛠️ Available Tools

### 🔢 Calculator
Safely evaluates mathematical expressions using Python.

```
Input:  "What is 345 * 918?"
Output: 316,710
```

### 🌐 Web Search _(Mock)_
Simulates search results — a clean placeholder for real API integration (SerpAPI, Tavily, etc.).

```
Input:  "Search latest AI trends"
Output: [Simulated search results]
```

---

## ⚙️ Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MohanGC07/Manual-Tool-Router-Agent.git
cd Manual-Tool-Router-Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ **Never commit your `.env` file.** Add it to `.gitignore`.

### 5. Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🔑 Getting a Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Navigate to **API Keys** and generate a new key
4. Paste it into your `.env` file

---

## 🗺️ Roadmap

- [ ] Add real web search via Tavily or SerpAPI
- [ ] Support multi-step / chained tool calls
- [ ] Add memory across turns
- [ ] Implement a ReAct-style loop
- [ ] Deploy to Streamlit Cloud

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or file an issue.

---

<p align="center">
  Built to learn. Built to extend. Built for the curious. 🧠
</p>