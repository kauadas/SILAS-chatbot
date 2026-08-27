from nlu.intent import detect_intent
from dialogue.manager import DialogueManager


def main() -> None:
    manager = DialogueManager()
    print("Chatbot iniciado. Digite 'sair' para encerrar.")

    while True:
        try:
            text = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAté mais!")
            break

        if not text:
            continue
        if text.lower() in {"sair", "exit", "quit"}:
            print("Bot: Até mais!")
            break

        intent = detect_intent(text)
        response = manager.respond(intent, text)

        print(f"Bot: {response}")
        print(f"[intent={intent.name} confidence={intent.confidence:.2f}]")


if __name__ == "__main__":
    main()
