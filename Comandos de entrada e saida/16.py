'''
Elabore um algoritmo que leia dois números inteiros e imprima a seguinte saída:
Dividendo:
Divisor:
Quociente:
Resultado da divisão inteira
Resto:
Para a resolução desse algoritmo utilize / , // e %.
'''
Dividendo = int(input("Informe o Dividendo: "))
Divisor = int(input("Informe o Divisor: "))
Quociente = Dividendo / Divisor
divisao_Inteira = Dividendo // Divisor
Resto = Dividendo % Divisor
print(f"Dividendo: {Dividendo}\nDivisor: {Divisor}\nQuociente: {Quociente}\nResultado da divisão inteira: {divisao_Inteira}\nResto: {Resto}")