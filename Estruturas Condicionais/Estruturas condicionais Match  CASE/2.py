operador = str(input("Informe a operação: "))

match operador:
    case '+':
        print("Adição")
    case '-':
        print("Subtração")
    case '/':
        print("Divisão")
    case '*':
        print("Multiplicação")
    case _:
        print('Outra operação')
