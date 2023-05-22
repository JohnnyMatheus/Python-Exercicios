'''Um banco concederá um crédito especial aos seus clientes de acordo com o saldo médio no último ano.
Faça um programa que leia o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela.
Ao final deve ser mostrado o saldo médio e o valor do crédito.


    Saldo médio (R$)                Crédito
    Acima de 4000,00            30% do saldo médio
    de 3001,00 a 4000,00        25% do saldo médio
    de 2001,00 a 3000,00        20% do saldo médio
    até 2000,00                 10% do saldo médio
'''

saldoMedio = float(input("Informe o saldo médio: "))

if(saldoMedio > 4000.00):
    valorCredito = (saldoMedio *30 /100)
    print(f"Saldo médio = {saldoMedio}\n"
          f"Valor do credito = {valorCredito}")
elif(saldoMedio >= 3001.00) and(saldoMedio <= 4000.00):
    valorCredito = (saldoMedio * 25 / 100)
    print(f"Saldo médio = {saldoMedio}\n"
          f"Valor do credito = {valorCredito}")
elif(saldoMedio >= 2001.00) and (saldoMedio <= 3000.00):
    valorCredito = (saldoMedio * 20 / 100)
    print(f"Saldo médio = {saldoMedio}\n"
          f"Valor do credito = {valorCredito}")
else:
    valorCredito = (saldoMedio * 10 / 100)
    print(f"Saldo médio = {saldoMedio}\n"
          f"Valor do credito  = {valorCredito}")