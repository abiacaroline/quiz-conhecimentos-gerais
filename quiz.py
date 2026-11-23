pontuacao_final = 0

def verificar_resposta(resposta_correta):
    resposta = input("Sua resposta: ").upper()

    if resposta == resposta_correta:
        print("Parabéns! Você acertou! +10 pontos")
        return 10
    else:
        print("Resposta incorreta!")
        return 0

def menu():
    print("\n===== QUIZ MASTER =====")
    print("1 - Iniciar Quiz")
    print("2 - Consultar pontuação")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    return opcao

def iniciar_quiz():
    global pontuacao_final
    pontuacao_final = 0

    print("\n===== QUIZ MASTER =====")

    print("\n1) Qual é a capital do Brasil?")
    print("A) São Paulo")
    print("B) Brasília")
    print("C) Rio de Janeiro")
    print("D) Salvador")

    pontuacao_final += verificar_resposta("B")

    print("\n2) Quantos planetas existem no Sistema Solar?")
    print("A) 7")
    print("B) 8")
    print("C) 9")
    print("D) 10")

    pontuacao_final += verificar_resposta("B")

    print("\n3) Qual é o maior oceano do mundo?")
    print("A) Atlântico")
    print("B) Índico")
    print("C) Pacífico")
    print("D) Ártico")

    pontuacao_final += verificar_resposta("C")

    print("\nSua pontuação final foi:", pontuacao_final, "pontos!")

def consultar_pontuacao():
    print("\n===== SUA PONTUAÇÃO =====")
    print("Pontuação da última partida:", pontuacao_final, "pontos")

def sair():
    print("\nObrigado por jogar o Quiz Master!")
    print("Até a próxima! 👋")

while True:
    opcao = menu()

    if opcao == "1":
        iniciar_quiz()

    elif opcao == "2":
        consultar_pontuacao()

    elif opcao == "3":
        sair()
        break

    else:
        print("Opção inválida! Tente novamente.")
