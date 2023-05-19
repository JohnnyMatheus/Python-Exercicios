'''Para vários tributos, a base de cálculo é o salário mínimo.
Elabore um algoritmo que leia o valor do salário mínimo e o valor do salário de uma pessoa.
Calcular e mostrar quantos salários mínimos essa pessoa ganha.
'''

salarioMinimo = float(input("Informe o valor do salário mínimo: "))
salario = float(input("Informe seu salário: "))

calculo = salario / salarioMinimo
print(f"Você recebe {calculo} salários mínimos")