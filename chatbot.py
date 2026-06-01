#!/usr/bin/env python3

import sys
from ollama import Client, ResponseError

MODEL = "llama3.2"
SYSTEM_PROMPT = (
    "You are a helpful, concise, and friendly assistant. "
    "Answer clearly and accurately."
)


def build_client() -> Client:
    return Client()


def chat(client: Client, history: list[dict]) -> str:
    response = client.chat(model=MODEL, messages=history)
    return response.message.content


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

        try:
            reply = chat(client, history)
        except ResponseError as exc:
            print(f"[Error] Ollama returned an error: {exc}\n")
            history.pop()
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"[Error] Unexpected error: {exc}\n")
            history.pop()
            continue

        history.append({"role": "assistant", "content": reply})
        print(f"\nAssistant: {reply}\n")


if __name__ == "__main__":
    run()
