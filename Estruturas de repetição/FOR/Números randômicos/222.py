import random

# Inicializa a variável do maior valor com o menor valor possível
maior_valor = 50

# Gera e exibe os 10 números aleatórios
for _ in range(10):
    numero = random.randint(50, 100)
    print(numero)

    # Verifica se o número gerado é maior que o maior valor atual
    if numero > maior_valor:
        maior_valor = numero

# Exibe o maior valor gerado
print("O maior valor gerado foi:", maior_valor)
