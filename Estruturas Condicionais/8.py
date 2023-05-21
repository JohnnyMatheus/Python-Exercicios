'''
Um comerciante comprou um produto e quer vendê-lo com um lucro de
45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
Elabore um algoritmo que leia o valor do produto, calcule e imprima
o valor de venda do produto.
'''

produto = float(input("Informe o valor do produto: "))

if(produto < 20.00):
    lucro = produto +((produto * 45)/100)
    print(f"Valor de venda do produto com lucro de 45% R$: {lucro:.2f}")
else:
    lucro = produto + ((produto * 30) / 100)
    print(f"Valor de venda do produto com lucro de 30% R$: {lucro:.2f}")