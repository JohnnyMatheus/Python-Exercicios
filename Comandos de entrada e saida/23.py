'''Calcular o salário de um funcionário que teve um aumento.
O sistema deve ler o salário inicial do funcionário e o percentual de aumento.
O sistema deve informar o valor do aumento e o novo salário do funcionário.'''

salario_Inicial = float(input("Informe seu salário atual: "))
percentualAumento = float(input("Informe o percentual de aumento: "))
aumento = (salario_Inicial*percentualAumento)/100
print(f"O valor do aumento sera de R$ {aumento} reais")
novoSalario = salario_Inicial + aumento
print(f"O novo salário do funcionário será R$ {novoSalario} reais")