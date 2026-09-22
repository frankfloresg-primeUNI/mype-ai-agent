# 🤖 MYPE AI Agent

A simple AI agent built with **Python, LangChain, LangGraph and Gemini**.
The project demonstrates how to connect an LLM with custom tools and control the agent flow using a graph.

---

## 🚀 Overview

This project implements a conversational AI agent capable of:

- 💬 Receiving user questions
- 🧠 Generating responses with Google Gemini
- 🔧 Calling custom tools when necessary
- 🔄 Routing between the AI agent and tool execution
- 🧩 Extracting and displaying only the final text response in the terminal

The project is designed as a practical introduction to **AI Agents, Tool Calling and LangGraph workflows**.

---

## 🛠️ Technologies

| Technology              | Purpose                             |
| ----------------------- | ----------------------------------- |
| **Python 3.10+**  | Main programming language           |
| **LangChain**     | LLM and tool integration            |
| **LangGraph**     | Agent workflow and state management |
| **Google Gemini** | Large Language Model                |
| **python-dotenv** | Environment variable management     |

---

## 📁 Project Structure

```text
mype-ai-agent/
│
├── src/
│   └── agent.py          # Main AI agent
│
├── .env                  # API key (DO NOT upload)
├── .gitignore            # Ignored files
├── README.md             # Project documentation
└── .venv/                # Python virtual environment
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/mype-ai-agent.git
cd mype-ai-agent
```

### 2. Create the virtual environment

```bash
py -3.10 -m venv .venv
```

### 3. Activate it

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -U langchain langgraph langchain-openai langchain-community faiss-cpu python-dotenv "mcp[cli]"
```

For the Gemini integration, make sure the corresponding Google Generative AI LangChain package is installed as well:

```bash
python -m pip install -U langchain-google-genai
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Do **not** commit your `.env` file to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
.venv/
__pycache__/
```

---

## ▶️ Run the Agent

From the project root:

```bash
python src/agent.py
```

The agent will process the configured question and print only the final response in the terminal.

Example:

```text
¡Claro que sí! Cuéntame, ¿en qué te puedo ayudar hoy?
```

---

## 🔧 Available Tools

### 📦 `consultar_stock(producto)`

Returns the available stock for a product.

Example:

```text
Laptop Lenovo → 8 unidades
Monitor LG → 15 unidades
Mouse Logitech → 25 unidades
Teclado Redragon → 10 unidades
```

### 💰 `calcular_descuento(precio, porcentaje)`

Calculates the final price after applying a discount.

Example:

```text
Precio: 100
Descuento: 20%

Resultado: 80
```

---

## 🧠 How the Agent Works

The workflow is built with **LangGraph**:

```text
            ┌─────────────┐
            │    START    │
            └──────┬──────┘
                   ↓
            ┌─────────────┐
            │    AGENT    │
            │   Gemini    │
            └──────┬──────┘
                   │
          ┌────────┴────────┐
          │                 │
     Tool call?          No tool
          │                 │
          ↓                 ↓
   ┌─────────────┐        END
   │    TOOLS    │
   └──────┬──────┘
          │
          └──────────→ AGENT
```

The agent decides whether it needs to call a tool. If a tool is required, `ToolNode` executes it and sends the result back to the agent.

---

## 🧩 Main Concepts

This project provides practice with:

- **LLM integration**
- **Prompt → response workflows**
- **Tool calling**
- **LangChain tools**
- **LangGraph StateGraph**
- **MessagesState**
- **Conditional routing**
- **Environment variables**
- **Virtual environments**
- **Python project structure**

---

## 🔐 Security

Never upload your API key to GitHub.

Bad:

```env
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXX
```

inside a committed file.

Good:

```env
GOOGLE_API_KEY=your_key_here
```

inside a local `.env` file that is ignored by Git.

---

## 📌 Project Status

🟢 **Working prototype**

Current implementation includes:

- ✅ Gemini integration
- ✅ LangChain tools
- ✅ LangGraph agent flow
- ✅ Tool routing
- ✅ Stock lookup tool
- ✅ Discount calculation tool
- ✅ Clean terminal output

---

## 🔮 Next Steps

Possible improvements:

- Add more business tools
- Accept user input dynamically from the terminal
- Connect the agent to a database
- Add persistent conversation memory
- Build an API with FastAPI
- Add a web interface
- Integrate MCP tools
- Deploy the agent to the cloud

---

## 👨‍💻 Author

**Frank Flores**

Electronic Engineering student transitioning into **AI Engineering, Machine Learning and Software Development**.

---

## ⭐ Learning Goal

This project is part of my hands-on learning journey in **AI Engineering and Agentic AI**, with a focus on building practical systems instead of only studying theory.
