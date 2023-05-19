'''Ana Maria recebeu seu salário e precisa pagar 2 contas que já venceram. Como as contas estão atrasadas,
Ana Maria terá que pagar multa de 3% sobre cada conta.
Precisamos ajudar!
Vamos construir um programa que solicite o salário de Ana Maria e o valor de suas contas.
O programa deve calcular e mostrar o total de suas despesas e o quanto restará do salário
de Ana Maria após pagar as contas.
Lembre-se que não temos funções prontas para calcular percentual, assim, utilizamos “regra de três”
e realizamos multiplicações e divisões para obter o resultado desejado.
Vamos ajudar a Ana Maria?'''

multa = 3 /100
salario = float(input("Informe o salário de Ana Maria: "))
conta1 = float(input("Informe o valor da 1° conta: "))
conta2 = float(input("Informe o valor da 2° conta: "))

multa1 = conta1 * multa
multa2  = conta2 * multa
despesas1 = conta1 + multa1
despesas2 = conta2 + multa2
total_Despesas = despesas1 + despesas2
salario_Final = salario - total_Despesas
print(f"Valor Primeira multa R$: {multa1}")
print(f"Valor segunda multa R$: {multa2}")
print(f"Despesas totais R$: {total_Despesas}")
print(f"restará do salário de Ana Maria após pagar as contas R$: {salario_Final}")

