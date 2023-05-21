'''Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
Elabore um algoritmo que leia a altura e o sexo de uma pessoa (M/F), calcule e imprima seu peso ideal,
utilizando as seguintes fórmulas.

Para homens	(72,7 * altura) - 58
Para mulheres	(62,1 * altura) – 44,7
'''


altura = float(input("Informe sua altura: "))
sexo = str.upper(input("Informe Sexo - Digite M para homem e F para mulher: "))

if(sexo == 'M'):
    homem = (72.7 * altura) - 58
    print(f"Seu peso ideal será: {homem:.2f}")
elif(sexo == 'F'):
    mulher = (62.1 * altura) - 44.7
    print(f"Seu peso ideal será: {mulher:.2f}")
else:
    print("Valor inválido")
