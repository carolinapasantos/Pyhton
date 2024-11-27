def exibir_opcoes():
    print("Escolha uma das opções abaixo:")
    print("1. Votar no Candidato 1")
    print("2. Votar no Candidato 2")
    print("3. Ver total de votos")
    print("4. Anular voto")
    print("5. Sair")

def contar_votos():
    print(f"Total de votos para o Candidato 1: {votos_cand1}")
    print(f"Total de votos para o Candidato 2: {votos_cand2}")
    print(f"Total de votos nulos: {votos_nulos}")

# Variáveis de contagem de votos
votos_cand1 = 0
votos_cand2 = 0
votos_nulos = 0

while True:
    exibir_opcoes()

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        votos_cand1 += 1
        print("Voto computado para o Candidato 1.")
    elif escolha == "2":
        votos_cand2 += 1
        print("Voto computado para o Candidato 2.")
    elif escolha == "3":
        contar_votos()
    elif escolha == "4":
        votos_nulos += 1
        print("Voto nulo computado.")
    elif escolha == "5":
        print("Encerrando a votação...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Imprime o total de votos ao final
print("\nResultado final da votação:")
contar_votos()

