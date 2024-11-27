def calcular():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a sua escolha (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            operacao = "adição"
        elif escolha == '2':
            resultado = num1 - num2
            operacao = "subtração"
        elif escolha == '3':
            resultado = num1 * num2
            operacao = "multiplicação"
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                operacao = "divisão"
            else:
                return "Erro: Divisão por zero!"

        print(f"O resultado da {operacao} é: {resultado}")
    else:
        print("Escolha inválida!")

calcular()
