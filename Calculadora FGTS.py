print("*************************")
print("Recolhimento do FGTS")
print("*************************")
nome=input("Digite o nome do contribuinte: ")
cpf=int(input("Digite o CPF do contribuinte sem ponto e traço: "))
salario=float(input("Digite o salário do contribuinte R$: "))
fgts=salario*0.08
print(f"Nome: {nome}”)print(f“CPF: {cpf}")
print(f"Recolhimentodo FGTS: {fgts:.2f}")
