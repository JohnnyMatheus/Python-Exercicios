'''
Elabore um algoritmo que leia um número inteiro e imprima seu sucessor e seu antecessor.
Por exemplo, suponha que o usuário digite o número 7, o algoritmo deverá imprimir
(escrever) na tela o seu antecessor (número 6) e o seu sucessor (o número 8).
'''

numero = int(input("Informe um numero: "))
antecessor = numero - 1
sucessor = numero + 1

print(f"O Número digitado foi: {numero}\nSeu sucessor é: {sucessor}\nSeu antecessor é: {antecessor}")