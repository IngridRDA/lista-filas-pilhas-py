# ============================================================
# Verificador de parentetização usando pilha
# ============================================================
# Regra: cada "(" precisa ter um ")" correspondente, e o ")"
# nunca pode aparecer antes de existir um "(" aberto.

# ------------------------------------------------------------
# Função que verifica a expressão usando uma pilha
# ------------------------------------------------------------
def parenteses_corretos(expressao):
    pilha = []                         # pilha começa vazia

    for caractere in expressao:        # percorre a expressão da esquerda para a direita
        if caractere == "(":
            pilha.append(caractere)    # empilha cada "abre parênteses"

        elif caractere == ")":
            if len(pilha) == 0:        # "fecha" sem nenhum "abre" esperando
                return False           # exemplo: ")(" falha logo no primeiro caractere
            pilha.pop()                # desempilha o "abre" correspondente

    # No final, a pilha deve estar vazia.
    # Se sobrou algum "(", ele ficou sem o ")" correspondente.
    return len(pilha) == 0


# ------------------------------------------------------------
# Programa principal: repete até o usuário escolher sair
# ------------------------------------------------------------
while True:
    print("\nVerificador de parênteses")

    # Repete a solicitação até receber uma entrada válida.
    while True:
        entrada = input("Digite a expressão (ex.: ( ( ) ) ou (2+3)*(4-1)): ")

        # Remove espaços para tratar "( ( ) )" e "(())" da mesma forma.
        expressao = entrada.replace(" ", "")

        # Exige pelo menos um caractere para ser verificado.
        if expressao:
            break

        print("Aviso: digite uma expressão antes de pressionar ENTER.")

    # Mostra o resultado da verificação.
    if parenteses_corretos(expressao):
        print(f"Expressão {entrada!r}: CORRETA")
    else:
        print(f"Expressão {entrada!r}: INCORRETA")

    # Aceita respostas com ou sem maiúsculas e espaços ao redor.
    while True:
        continuar = input("Deseja verificar outra expressão? (s/n): ").strip().lower()
        if continuar in ("s", "sim", "n", "nao", "não"):
            break
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    # Encerra o laço principal se o usuário escolher não continuar.
    if continuar in ("n", "nao", "não"):
        break