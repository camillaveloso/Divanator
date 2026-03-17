def play(node):
    current = node

    while current is not None:
        if current.is_leaf():
            if isinstance(current.answer, list):
                print("\nNão consegui chegar em uma única resposta.")
                print("As possibilidades restantes são:")
                for option in current.answer:
                    print(f"- {option}")
            else:
                print(f"\n Você pensou em: {current.answer}")
            return

        answer = input(f"{current.question} (s/n): ").strip().lower()

        while answer not in ["s", "n"]:
            answer = input("Digite apenas 's' para sim ou 'n' para não: ").strip().lower()

        if answer == "s":
            current = current.yes
        else:
            current = current.no
