# ============================================================
# Intercalar duas filas
# ============================================================
# A função recebe duas filas e retorna uma nova fila com os
# elementos intercalados, respeitando a ordem de cada fila.

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
# Função que intercala as duas filas
# ------------------------------------------------------------
def intercalar_filas(fila1, fila2):
    resultado = deque()            # fila que vai receber os elementos intercalados

    # Enquanto as DUAS filas tiverem elementos, alterna entre elas:
    # um da fila 1, depois um da fila 2.
    while not fila_vazia(fila1) and not fila_vazia(fila2):
        enfileirar(resultado, desenfileirar(fila1))
        enfileirar(resultado, desenfileirar(fila2))

    # Uma das filas acabou. Se sobrou algo na fila 1, passa tudo para o final.
    while not fila_vazia(fila1):
        enfileirar(resultado, desenfileirar(fila1))

    # Se sobrou algo na fila 2, passa tudo para o final.
    while not fila_vazia(fila2):
        enfileirar(resultado, desenfileirar(fila2))

    return resultado


# ------------------------------------------------------------
# Programa principal: repete até o usuário escolher sair
# ------------------------------------------------------------
while True:
    print("\nIntercalação de filas")

    # Lê a fila 1 (pode ficar vazia se o usuário só apertar ENTER).
    entrada1 = input("Digite os elementos da fila 1 separados por espaço: ")
    elementos1 = entrada1.split()

    # Lê a fila 2 (também pode ficar vazia).
    entrada2 = input("Digite os elementos da fila 2 separados por espaço: ")
    elementos2 = entrada2.split()

    # Cria as filas com os elementos digitados.
    F1 = deque(elementos1)
    F2 = deque(elementos2)

    # Mostra as filas antes de intercalar.
    print("Fila 1:", list(F1))
    print("Fila 2:", list(F2))

    # Intercala as filas (isso esvazia F1 e F2).
    F3 = intercalar_filas(F1, F2)

    # Mostra a fila resultante.
    print("Fila intercalada:", list(F3))

    # Aceita respostas com ou sem maiúsculas e espaços ao redor.
    while True:
        continuar = input("Deseja intercalar outras filas? (s/n): ").strip().lower()
        # Só encerra a validação quando a resposta for sim ou não.
        if continuar in ("s", "sim", "n", "nao", "não"):
            break
        # Orienta o usuário quando a resposta não for reconhecida.
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    # Encerra o laço principal se o usuário escolher não continuar.
    if continuar in ("n", "nao", "não"):
        break