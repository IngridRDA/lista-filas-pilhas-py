# ============================================================
# Inverter uma fila usando uma pilha auxiliar
# ============================================================
# Usamos apenas as operações básicas da fila e da pilha.

from collections import deque

# ------------------------------------------------------------
# Operações da FILA (FIFO: primeiro a entrar, primeiro a sair)
# ------------------------------------------------------------
def enfileirar(fila, elemento):
    fila.append(elemento)          # insere no final da fila

def desenfileirar(fila):
    return fila.popleft()          # remove e devolve o elemento do início

def fila_vazia(fila):
    return len(fila) == 0


# ------------------------------------------------------------
# Operações da PILHA (LIFO: último a entrar, primeiro a sair)
# ------------------------------------------------------------
def empilhar(pilha, elemento):
    pilha.append(elemento)         # insere no topo da pilha

def desempilhar(pilha):
    return pilha.pop()             # remove e devolve o elemento do topo

def pilha_vazia(pilha):
    return len(pilha) == 0


# ------------------------------------------------------------
# Função que inverte a fila usando a pilha
# ------------------------------------------------------------
def inverter_fila(fila, pilha):
    # Etapa 1: move todos os elementos da fila para a pilha.
    # O primeiro da fila entra primeiro na pilha, ficando no fundo.
    while not fila_vazia(fila):
        elemento = desenfileirar(fila)
        empilhar(pilha, elemento)

    # Etapa 2: move todos os elementos da pilha de volta para a fila.
    # O topo da pilha (que era o último da fila) sai primeiro,
    # e passa a ser o primeiro da nova fila.
    while not pilha_vazia(pilha):
        elemento = desempilhar(pilha)
        enfileirar(fila, elemento)


# ------------------------------------------------------------
# Programa principal: repete até o usuário escolher sair
# ------------------------------------------------------------
while True:
    print("\nInversão de fila usando pilha")

    # Repete a solicitação até receber uma entrada válida.
    while True:
        entrada = input("Digite os elementos da fila separados por espaço: ")

        # split separa os elementos usando espaços.
        elementos = entrada.split()

        # A fila precisa ser não vazia (como pede o enunciado).
        if elementos:
            break

        print("Aviso: a fila não pode ser vazia. Digite pelo menos um elemento.")

    # Cria a fila com os elementos digitados e a pilha P vazia.
    F = deque(elementos)
    P = []

    # Mostra a fila antes da inversão.
    print("Fila antes: ", list(F))

    # Inverte a fila usando a pilha auxiliar.
    inverter_fila(F, P)

    # Mostra a fila depois da inversão e confirma que a pilha ficou vazia.
    print("Fila depois:", list(F))
    print("Pilha ao final:", P)

    # Aceita respostas com ou sem maiúsculas e espaços ao redor.
    while True:
        continuar = input("Deseja inverter outra fila? (s/n): ").strip().lower()
        # Só encerra a validação quando a resposta for sim ou não.
        if continuar in ("s", "sim", "n", "nao", "não"):
            break
        # Orienta o usuário quando a resposta não for reconhecida.
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    # Encerra o laço principal se o usuário escolher não continuar.
    if continuar in ("n", "nao", "não"):
        break