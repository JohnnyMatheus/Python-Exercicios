'''Uma empresa decidiu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
####################################
Salário Atual (R$)          AUMENTO#
0 - 1.000,00                 25%   #
1.000,01 – 2.000,00          20%   #
2.000,01- 3.000,00           15%   #
acima de 3.000,00            10%   #
####################################

Escrever um algoritmo que leia o salário atual de um funcionário e escreva:
- o percentual de seu aumento, de acordo com o salário atual
- o valor do aumento (em R$)
- o valor do salário corrigido a partir desse aumento.
'''

salario_Atual = float(input("Informe o salário do funcionário: "))

if(salario_Atual <= 1000.00):
    aumento = (salario_Atual * 25)/100
    novoSalario = salario_Atual + aumento
    print(f"Valor do aumento: R$ {aumento}\n"
          f"O valor do salário corrigido a partir desse aumento será R$ {novoSalario}")
elif(salario_Atual >=1000.01) and (salario_Atual <= 2000.00):
    aumento = (salario_Atual * 20) / 100
    novoSalario = salario_Atual + aumento
    print(f"Valor do aumento: R$ {aumento}\n"
          f"O valor do salário corrigido a partir desse aumento será R$ {novoSalario}")
elif(salario_Atual >= 2000.01) and (salario_Atual <= 3000.00):
    aumento = (salario_Atual * 15) / 100
    novoSalario = salario_Atual + aumento
    print(f"Valor do aumento: R$ {aumento}\n"
          f"O valor do salário corrigido a partir desse aumento será R$ {novoSalario}")
else:
    aumento = (salario_Atual * 10) / 100
    novoSalario = salario_Atual + aumento
    print(f"Valor do aumento: R$ {aumento}\n"
          f"O valor do salário corrigido a partir desse aumento será R$ {novoSalario}")
