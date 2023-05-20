'''Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e 90, ou não.'''

numero = int(input("Informe um Número: "))

if(numero > 20) and(numero < 90):
    print(f"O Número {numero} está compreendido entre 20 e 90")
elif(numero == 20) or (numero == 90):
    print("Por favor insira um número que esteja entre 20 e 90")
else:
    print("Não esta entre 20 e 90")


