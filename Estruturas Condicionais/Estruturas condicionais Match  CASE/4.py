'''Elabore um algoritmo que, tendo como dados de entrada o preço de um produto e um código de origem,
mostrar o preço e sua procedência. Caso o código não seja nenhum dos especificados,
o produto deve ser impresso como importado. Use a estrutura de condição MATCH/CASE para resolver este exercício

1 – Sul
2 – Norte
3 – Leste
4 – Oeste
5 ou 6 – Noroeste
7, 8 ou 9 - Sudeste
10 até 12– Centro-Oeste
13 até 15 – Nordeste
'''

precoProduto = float(input("Informe o valor do produto: "))
codigo = int(input("Informe o código do produto: "))

match codigo :
    case 1:
        print(f"Preço: R$ {precoProduto}\n"
              f"1 – Sul")
    case 2:
        print(f"Preço: R$ {precoProduto}\n"
              f"2 – Norte")
    case 3:
        print(f"Preço: R$ {precoProduto}\n"
              f"3 – Leste")
    case 4:
        print(f"Preço: R$ {precoProduto}\n"
              f"4 – Oeste")
    case 5 | 6:
        print(f"Preço: R$ {precoProduto}\n"
              f"5 ou 6 – Noroeste")
    case 7 | 8 | 9:
        print(f"Preço: R$ {precoProduto}")
        print("7, 8 ou 9 - Sudeste")
    case 10 | 11 | 12:
        print(f"Preço: R$ {precoProduto}")
        print("10 até 12– Centro-Oeste")

    case 13 | 14 | 15 :
        print(f"Preço: R$ {precoProduto}")
        print("13 até 15 – Nordeste")
    case _:
        print("Importado")