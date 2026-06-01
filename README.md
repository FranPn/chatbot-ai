# chatbot-ai

A lightweight terminal chatbot powered by [Ollama](https://ollama.com) and the **llama3.2** model. Supports multi-turn conversations — the full chat history is maintained in memory for the duration of each session.

---

## Requirements

| Requirement | Version |
|---|---|
| Python | 3.11+ |
| Ollama | latest |
| llama3.2 model | pulled via Ollama |

---

## Setup

### 1. Install Ollama

Follow the official instructions at the Ollama website, then pull the model:

```bash
ollama pull llama3.2
```

### 2. Clone the repository

```bash
git clone <your-repo-url>
cd chatbot-ai
```

### 3. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage

Make sure the Ollama server is running (`ollama serve` if not already started), then:

```bash
python chatbot.py
```

Example session:

```
Chatbot (model: llama3.2) — type 'exit' or press Ctrl+C to quit.

You: What is the capital of France?

Assistant: The capital of France is Paris.

You: And what language do they speak there?

Assistant: They speak French in Paris and throughout France.

You: exit
Goodbye!
```

To end the session type `exit`, `quit`, `bye`, or press **Ctrl+C**.

---

## Configuration

The model and system prompt can be changed by editing the constants at the top of `chatbot.py`:

```python
MODEL = "llama3.2"
SYSTEM_PROMPT = "You are a helpful, concise, and friendly assistant."
```

---

## Project structure

```
chatbot-ai/
├── chatbot.py        # Main application
├── requirements.txt  # Python dependencies
└── README.md
```

---

## License

MIT
