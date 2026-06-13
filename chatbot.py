#!/usr/bin/env python3

import sys
from ollama import Client, ResponseError

MODEL = "llama3.2"
SYSTEM_PROMPT = (
    "You are a helpful, concise, and friendly assistant. "
    "Answer clearly and accurately."
)
MAX_HISTORY_MESSAGES = 20  # excluding system prompt


def build_client() -> Client:
    return Client()


def chat_stream(client: Client, history: list[dict]):
    response = client.chat(model=MODEL, messages=history, stream=True)
    for chunk in response:
        yield chunk.message.content


def trim_history(history: list[dict]) -> None:
    if len(history) > MAX_HISTORY_MESSAGES + 1:
        history[:] = [history[0]] + history[-MAX_HISTORY_MESSAGES:]


def run() -> None:
    client = build_client()
    history: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]

    print(f"Chatbot (model: {MODEL}) — type 'exit' or press Ctrl+C to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit(0)

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Goodbye!")
            sys.exit(0)

        history.append({"role": "user", "content": user_input})

        print("\nAssistant: ", end="", flush=True)
        reply_parts: list[str] = []
        try:
            for piece in chat_stream(client, history):
                print(piece, end="", flush=True)
                reply_parts.append(piece)
        except ResponseError as exc:
            print(f"\n[Error] Ollama returned an error: {exc}\n")
            history.pop()
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"\n[Error] Unexpected error: {exc}\n")
            history.pop()
            continue

        print("\n")
        history.append({"role": "assistant", "content": "".join(reply_parts)})
        trim_history(history)


if __name__ == "__main__":
    run()
