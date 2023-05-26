estoque = 0
produto = 0
somar = 0
fim = True
print("1 - Acrescentar produto\n"
      "2 - Retirar produto\n"
      "3 - Mostrar a quantidade de produto no estoque\n"
      "4 - Sair")

while fim:
    opcao = int(input("Informe a opção que deseja: "))
    match opcao:
        case 1:
            estoque = int(input("Quantos produtos deseja adicionar: "))
            qtdEstoque = estoque + produto
        case 2 :
            retirar = int(input("Informe a quantidade que deseja remover: "))
            if(retirar < estoque):
                qtdEstoque = qtdEstoque - retirar
            else:
                print(f"Temos apenas {qtdEstoque} em estoque ")

        case 3 :
            print("3 - Mostrar ")
            produto = qtdEstoque
            print(f"Quantidade de produtos disponível no estoque {produto}")
        case 4 :
            print("Programa finalizado")
            fim = False
            break
        case _:
            print("Opção inválida!")