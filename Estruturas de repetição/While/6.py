'''Elabore um algoritmo que leia a idade e sexo (M – masculino, F – feminino) de várias pessoas
(solicite ao usuário o número total de pessoas que devem ter seus dados lidos). Calcule e imprima:

- a idade média de todas as pessoas;
- o número de pessoas do sexo feminino;
- o número pessoas do sexo masculino com idade entre 15 e 20 anos inclusive.'''

total_pessoas = int(input("Digite o número total de pessoas: "))

soma_idades = 0
num_feminino = 0
num_masculino_idade_15_20 = 0

for _ in range(total_pessoas):
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")

    soma_idades += idade

    if sexo.upper() == "F":
        num_feminino += 1

    if sexo.upper() == "M" and idade >= 15 and idade <= 20:
        num_masculino_idade_15_20 += 1

media_idades = soma_idades / total_pessoas

print("Idade média de todas as pessoas:", media_idades)
print("Número de pessoas do sexo feminino:", num_feminino)
print("Número de pessoas do sexo masculino com idade entre 15 e 20 anos:", num_masculino_idade_15_20)
