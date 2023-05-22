'''Criar um algoritmo que leia dois números inteiros, e que solicite ao usuário qual a operação que
ele deseja realizar entre esses números.
Caso o usuário digitar o caractere ‘*’ será realizada uma multiplicação,
caso seja digitado o caractere ‘/’ será realizada uma divisão,
caso seja digitado o caractere ‘+’ será realizado uma adição entre os números,
e caso seja digitado o caractere ‘-’ será realizada uma subtração.
Utilize a estrutura de condição MATCH/CASE.
'''

numero1 = int(input("Informe o 1° número: "))
numero2 = int(input("Informe o 2° número: "))
print("Informe a operação que deseja realizar\n"
                     "Digite * para multiplicar\n"
                     "Digite / para dividir\n"
                     "Digite + para somar\n"
                     "Digite - para subtrair")
operacao = str(input())
match operacao:
    case '*':
        multiplicacao = numero1 * numero2
        print(f" {numero1} X {numero2} = {multiplicacao} ")
    case '/':
        divisao = numero1 / numero2
        print(f"{numero1} / {numero2} = {divisao}")
    case '+':
        somar = numero1 + numero2
        print(f"{numero1} + {numero2} = {somar}")
    case '-':
        subtracao = numero1 - numero2
        print(f"{numero1} - {numero2} = {subtracao}")
    case _:
        print("Inválido")