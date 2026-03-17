from tree import get_root
from search import dfs, bfs
from game import play


def main():
    root = get_root()

    while True:
        print("\n===== DIVANATOR <3 =====")
        print("1 - Jogar")
        print("2 - Mostrar DFS")
        print("3 - Mostrar BFS")
        print("4 - Sair")

        option = input("Escolha uma opção: ").strip()

        if option == "1":
            print("\nPense em uma diva ou grupo musical <3")
            play(root)

        elif option == "2":
            print("\n=== Percurso DFS ===")
            dfs(root)

        elif option == "3":
            print("\n=== Percurso BFS ===")
            bfs(root)

        elif option == "4":
            print("Brigada por jogar Divanator conosco, até a próxima <3")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
