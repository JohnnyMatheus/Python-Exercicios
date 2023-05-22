'''Construir um algoritmo que solicite um número inteiro.
Em seguida o algoritmo deve multiplicar por 2 número lido e mostrar o resultado.
O resultado deve ser multiplicado por 2 e mostrado outras tantas vezes enquanto o usuário responder
S (Sim) a pergunta “Deseja continuar (S/N) ?'''

numero = int(input("Digite um número inteiro: "))
resultado = numero * 2

print("O resultado é:", resultado)

continuar = input("Deseja continuar (S/N)? ")

while continuar.upper() == "S":
    resultado *= 2
    print("O resultado é:", resultado)
    continuar = input("Deseja continuar (S/N)? ")

print("Fim do programa.")