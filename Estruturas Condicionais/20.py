'''Um comerciante calcula o valor de venda dos produtos a partir do do valor que
ele compra os produtos e tendo em vista a tabela a seguir:

        VALOR DA COMPRA                    VALOR DA VENDA
        Valor < R$ 10,00                    Lucro de 70%
    R$ 10,00 <= valor < R$ 30,00            Lucro de 50%
    R$ 30,00 <= valor < R$ 50,00            Lucro de 40%
        Valor >= R$ 50,00                   Lucro de 30%

Elabore um algoritmo que possa entrar com o nome do produto e o valor de compra e que imprima o nome
do produto e o valor de venda.
'''

nomeProduto = str(input("Informe o nome do Produto: "))
valorCompra = float(input("Informe o valor de compra: "))

if(valorCompra < 10.00):
    lucro = valorCompra + ((valorCompra*70)/100)
    valorVenda = lucro
    print(f"{nomeProduto}: valor de venda R$: {valorVenda}")
elif(valorCompra < 30):
    lucro = valorCompra + ((valorCompra * 50) / 100)
    valorVenda = lucro
    print(f"{nomeProduto}: valor de venda R$: {valorVenda}")
elif(valorCompra < 50):
    lucro = valorCompra + ((valorCompra * 40) / 100)
    valorVenda = lucro
    print(f"{nomeProduto}: valor de venda R$: {valorVenda}")
else:
    lucro = valorCompra + ((valorCompra * 30) / 100)
    valorVenda = lucro
    print(f"{nomeProduto}: valor de venda R$: {valorVenda}")