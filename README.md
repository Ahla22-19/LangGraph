# LangGraph Chatbot Development

A practical exploration of LangGraph through conversational AI implementations.

## 📋 Overview

This repository contains chatbot implementations built with LangGraph, demonstrating progressive complexity in conversational AI architecture. Each implementation explores different aspects of LangGraph's capabilities for building stateful, multi-actor LLM applications.

## 🏗️ Repository Structure

```

.
├── Chatbot.py          # Core chatbot implementation
├── Simple_Bot.py       # Foundational bot structure
├── .gitignore
└── README.md

```

## 💻 Technical Stack

- **LangGraph** - Stateful multi-actor LLM application framework
- **Python 3.9+** - Primary programming language
- **LangChain** - LLM application development framework

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Ahla22-1/learning-langgraph.git
cd learning-langgraph
```

1. Install dependencies:

```bash
pip install langgraph langchain python-dotenv
```

1. Configure environment variables:

```bash
# Create .env file with your API credentials
OPENAI_API_KEY=your_api_key_here
```

📖 Implementation Details

Simple_Bot.py

Basic chatbot implementation demonstrating core LangGraph concepts including graph structure, nodes, and basic conversation flow.

Chatbot.py

Enhanced implementation featuring:

· State management
· Conversation memory
· Improved response handling
· Error management

🔧 Usage

Run individual bot implementations:

```bash
# Execute basic bot
python Simple_Bot.py

# Run enhanced chatbot
python Chatbot.py
```

📚 Documentation

· LangGraph Documentation
· LangChain Documentation

📄 License

MIT License - see LICENSE file for details

👤 Author

Ahla22-19
