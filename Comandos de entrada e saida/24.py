'''João recebeu seu salário e precisa pagar as contas da casa (água, luz e telefone celular).
Construir um programa que solicite o salário de João, o valor de suas contas,
calcule e mostre suas despesas e o quanto restará do salário de João.'''

salario = float(input("Informe o seu salário: "))
agua = float(input("Informe o valor da conta de água: "))
luz = float(input("Informe o valor da conta de luz: "))
telCelular = float(input("Informe o valor da conta do telefone celular: "))
despesas = agua + luz + telCelular
print(f"Valor das despesas: {despesas}")
salarioFinal= salario - despesas
print(f"Restará do salário de João: R$ {salarioFinal}")