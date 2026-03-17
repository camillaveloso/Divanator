from collections import deque


def _format_candidates(candidates, limit=8):
    if not candidates:
        return "nenhuma"

    if len(candidates) <= limit:
        return ", ".join(candidates)

    visible = ", ".join(candidates[:limit])
    remaining = len(candidates) - limit
    return f"{visible} ... (+{remaining})"


def dfs(node, depth=0, branch="RAIZ"):
    if node is None:
        return

    indent = "    " * depth

    print(f"\n{indent}[{branch}]")
    print(f"{indent}Opções restantes ({len(node.candidates)}): {_format_candidates(node.candidates)}")

    if node.question is not None:
        print(f"{indent}Pergunta: {node.question}")
    else:
        print(f"{indent}Resposta final: {node.answer}")
        return

    dfs(node.yes, depth + 1, "SIM")
    dfs(node.no, depth + 1, "NÃO")


def bfs(root):
    if root is None:
        return

    queue = deque([(root, 0, "RAIZ", "Início da árvore")])
    node_number = 1

    print("\n========== BFS ==========")
    print("Exploração por nível da árvore:\n")

    while queue:
        node, level, branch, parent_question = queue.popleft()

        print(f"--- Nó {node_number} | Nível {level} | Ramo: {branch} ---")
        print(f"Veio de: {parent_question}")
        print(f"Opções restantes ({len(node.candidates)}): {_format_candidates(node.candidates)}")

        if node.question is not None:
            print(f"Pergunta atual: {node.question}")
        else:
            print(f"Resposta final: {node.answer}")

        print("-" * 50)

        if node.yes is not None:
            queue.append((node.yes, level + 1, "SIM", node.question))

        if node.no is not None:
            queue.append((node.no, level + 1, "NÃO", node.question))

        node_number += 1


