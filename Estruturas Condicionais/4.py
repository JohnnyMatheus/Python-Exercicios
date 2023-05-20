'''Elabore um algoritmo que leia dois números e responda se a divisão do primeiro pelo segundo é
exata (o resto da divisão deve ser igual a 0).
Se for, o algoritmo deve imprimir a mensagem “A divisão de (1º numero) por (2º número) é exata”.'''

numero1 = int(input("Informe o 1° número: "))
numero2 = int(input("Informe o 2° número: "))

if(numero1 % numero2 ==0):
    print(f"A divisão de {numero1} por {numero2} é exata")
else:
    print("A divisão não é exata")
    