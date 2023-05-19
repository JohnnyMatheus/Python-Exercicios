'''
Ler 2 valores para as variáveis A e B.
Em seguida efetuar a troca dos valores de forma que a variável A passe a ter o valor da variável B e que a
variável B passe a ter o valor da variável A.
Devem ser mostrados os valores lidos, realizar a troca e em seguida apresentar os valores trocados.
'''

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
aux =a
a = b
b = aux

print(f"Valor de A {a} e valor de B {b}")
