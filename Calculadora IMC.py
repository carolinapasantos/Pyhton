print("*************************")
print("Calculadora de IMC")
print("*************************")
print("\n")
nome=input("Digite o nome do Paciente: ")
idade=int(input("Digite a idade do Paciente: "))
peso=float(input("Digite o peso do Paciente: "))
altura=float(input("Digite a altura do Paciente: "))
imc=peso/(altura**2)
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"IMC: {imc:.2f}")
