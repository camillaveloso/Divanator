# Divanator <3

Divanator é um jogo de adivinhação inspirado no Akinator, desenvolvido em Python para a disciplina de Estrutura de Dados Avançados, do professor Amaury Nogueira.
O jogo foi desenvolvido pelas integrantes Camila Menezes, Camilla Veloso e Pietra Bezerra.

O sistema utiliza uma árvore de decisão binária para tentar adivinhar em qual diva da cultura pop ou grupo musical o usuário pensou, por meio de perguntas de Sim ou Não no terminal.

Além do jogo interativo, o projeto também implementa os algoritmos de DFS (Depth-First Search) e BFS (Breadth-First Search) para percorrer a árvore e demonstrar, na prática, a diferença entre busca em profundidade e busca em largura.

---

## Objetivo do projeto

O objetivo do trabalho é aplicar conceitos de árvores binárias e algoritmos de busca em um sistema simplificado de adivinhação.

No Divanator:

- cada nó interno da árvore representa uma pergunta;
- cada folha representa uma resposta final, ou seja, uma diva ou grupo musical;
- as respostas "sim" e "não" determinam o caminho percorrido na árvore.

---

## Estruturas e algoritmos utilizados

O projeto foi desenvolvido com base nos seguintes conceitos:

- Árvore binária de decisão
- Busca em Profundidade (DFS)
- Busca em Largura (BFS)
- Fila para implementação do BFS
- Recursão para implementação do DFS
- Entrada interativa no terminal com respostas `s/n`

---

## Funcionamento do jogo

Ao iniciar o programa, o usuário escolhe uma das opções disponíveis no menu:

- jogar normalmente;
- exibir o percurso em DFS;
- exibir o percurso em BFS;
- encerrar o programa.

No modo de jogo:

1. o sistema inicia na raiz da árvore;
2. faz uma pergunta ao usuário;
3. recebe uma resposta `s` ou `n`;
4. segue pelo ramo correspondente;
5. repete o processo até chegar a uma resposta final.

Exemplo de execução:

É um grupo? (s/n): n
Estreou nos anos 00? (s/n): s
É dos Estados Unidos? (s/n): s
O estilo principal é R&B? (s/n): s

Você pensou em: Beyoncé
