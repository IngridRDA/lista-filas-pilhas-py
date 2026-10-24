# ============================================================
# Programa: contar elementos pares de uma pilha (recursivo)
# ============================================================

# ------------------------------------------------------------
# Função recursiva contaPar
# ------------------------------------------------------------
def contaPar(pilha):
    # Caso base: pilha vazia, não há mais elementos para contar
    if len(pilha) == 0:
        return 0

    # Retira o elemento do topo da pilha
    topo = pilha.pop()

    # Caso recursivo: se o topo for par, conta 1 e soma com o resto
    if topo % 2 == 0:
        return 1 + contaPar(pilha)
    # Se for ímpar, não conta e segue para o resto da pilha
    else:
        return contaPar(pilha)


# ------------------------------------------------------------
# Função auxiliar: lê os números digitados pelo usuário
# ------------------------------------------------------------
def ler_pilha(mensagem):
    entrada = input(mensagem)              # lê o texto digitado
    try:
        # separa por espaço e converte cada item para inteiro
        return [int(x) for x in entrada.split()]
    except ValueError:
        # se digitar letras ou símbolos, avisa e retorna None
        print("Erro: digite apenas números inteiros separados por espaço.")
        return None


# ------------------------------------------------------------
# Caso 1: pilha vazia
# ------------------------------------------------------------
def caso_vazia():
    print("\n--- Caso 1: pilha vazia ---")
    pilha = []                             # pilha começa sem elementos
    print("Pilha:", pilha)
    print("Quantidade de pares:", contaPar(pilha.copy()))
    # saída esperada: 0


# ------------------------------------------------------------
# Caso 2: pilha só com ímpares
# ------------------------------------------------------------
def caso_impares():
    print("\n--- Caso 2: pilha só com ímpares ---")
    pilha = ler_pilha("Digite números ímpares separados por espaço: ")
    if pilha is None:                      # entrada inválida
        return

    # Validação: se algum número for par, avisa o usuário
    if any(x % 2 == 0 for x in pilha):
        print("Atenção: você digitou número(s) par(es)! Digite apenas ímpares.")
    else:
        print("Pilha:", pilha)
        # usa .copy() para não perder a pilha original (pop() remove itens)
        print("Quantidade de pares:", contaPar(pilha.copy()))
        # saída esperada: 0


# ------------------------------------------------------------
# Caso 3: pilha só com pares
# ------------------------------------------------------------
def caso_pares():
    print("\n--- Caso 3: pilha só com pares ---")
    pilha = ler_pilha("Digite números pares separados por espaço: ")
    if pilha is None:
        return

    # Validação: se algum número for ímpar, avisa o usuário
    if any(x % 2 != 0 for x in pilha):
        print("Atenção: você digitou número(s) ímpar(es)! Digite apenas pares.")
    else:
        print("Pilha:", pilha)
        print("Quantidade de pares:", contaPar(pilha.copy()))
        # saída esperada: quantidade total de números digitados


# ------------------------------------------------------------
# Caso 4: pilha mista (pares e ímpares)
# ------------------------------------------------------------
def caso_mista():
    print("\n--- Caso 4: pilha mista ---")
    pilha = ler_pilha("Digite números (pares e ímpares) separados por espaço: ")
    if pilha is None:
        return

    pares = contaPar(pilha.copy())         # conta os pares
    impares = len(pilha) - pares           # o resto são ímpares

    print("Pilha:", pilha)
    print("Quantidade de pares:", pares)
    print("Quantidade de ímpares:", impares)


# ------------------------------------------------------------
# Programa principal: menu que repete até o usuário sair
# ------------------------------------------------------------
def main():
    while True:
        print("\n==============================")
        print("   CONTADOR DE PARES (PILHA)  ")
        print("==============================")
        print("1 - Pilha vazia")
        print("2 - Pilha só com ímpares")
        print("3 - Pilha só com pares")
        print("4 - Pilha mista")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            caso_vazia()
        elif opcao == "2":
            caso_impares()
        elif opcao == "3":
            caso_pares()
        elif opcao == "4":
            caso_mista()
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break                          # sai do loop
        else:
            print("Opção inválida! Tente novamente.")


# Executa o programa principal
main()