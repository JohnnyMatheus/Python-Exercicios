'''Elabore um algoritmo que leia a idade e o estado civil (C – casado, S – solteiro, V – viúvo, e
D – divorciado ou T - convivente) de várias pessoas.
Considere que o algoritmo termina quando se digita ‘N’ como resposta à pergunta “Deseja continuar (S/N)?’.
Ao final, calcule e imprima:
A quantidade de pessoas casadas;
A idade da pessoa solteira mais velha
A média das idades das pessoas viúvas;
A porcentagem de pessoas conviventes, dentre todas as pessoas analisadas.'''

# Variáveis para armazenar os resultados
quantidade_casados = 0
idade_solteiro_mais_velho = 0
soma_idades_viuvos = 0
quantidade_viuvos = 0
quantidade_conviventes = 0
total_pessoas = 0

# Loop principal para ler os dados das pessoas
continuar = True
while continuar:
    idade = int(input("Digite a idade: "))
    estado_civil = input("Digite o estado civil (C - casado, S - solteiro, V - viúvo, D - divorciado ou T - convivente): ")

    if estado_civil == 'C':
        quantidade_casados += 1
    elif estado_civil == 'S':
        if idade > idade_solteiro_mais_velho:
            idade_solteiro_mais_velho = idade
    elif estado_civil == 'V':
        soma_idades_viuvos += idade
        quantidade_viuvos += 1
    elif estado_civil == 'T':
        quantidade_conviventes += 1

    total_pessoas += 1

    resposta = input("Deseja continuar (S/N)? ")
    if resposta == 'N':
        continuar = False

# Cálculo dos resultados
media_idades_viuvos = soma_idades_viuvos / quantidade_viuvos if quantidade_viuvos > 0 else 0
porcentagem_conviventes = (quantidade_conviventes / total_pessoas) * 100 if total_pessoas > 0 else 0

# Impressão dos resultados
print("Quantidade de pessoas casadas:", quantidade_casados)
print("Idade da pessoa solteira mais velha:", idade_solteiro_mais_velho)
print("Média das idades das pessoas viúvas:", media_idades_viuvos)
print("Porcentagem de pessoas conviventes:", porcentagem_conviventes)
