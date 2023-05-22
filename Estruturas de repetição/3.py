escritor = []
while True:
    nome = str(input("Informe o nome do escritor: "))
    idade = int(input("Informe a idade: "))
    qtd_Livros = int(input("Informe a quantidade de livros: "))

    escritor.append((nome,idade,qtd_Livros))

    opcao = input("Deseja adicionar outro escritor? (s/n): ")
    if opcao.lower() != 's':
        break


mais_novo = escritor[0]
mais_velho = escritor[0]
maislivros = escritor[0]


for escritor in escritor:
    if escritor[1] < mais_novo[1]:
        mais_novo = escritor
    if escritor[1] > mais_velho[1]:
        mais_velho = escritor
    if escritor[2] > maislivros[2]:
        escritor_mais_livros = escritor
#############################################
print("Listando")
print("Escritor mais novo:")
print("Nome:", mais_novo[0])
print("Idade:", mais_novo[1])
print("Escritor mais velho:")
print("Nome:", mais_velho[0])
print("Quantidade de livros:", mais_velho[2])
print("Escritor com maior quantidade de livros:")
print("Nome:", maislivros[0])
####################################################
