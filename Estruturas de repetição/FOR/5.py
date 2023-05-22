'''Elabore um algoritmo que leia nome e a idade de 20 pessoas.
Imprimir o nome na seguinte mensagem se a pessoa tiver mais de 18 anos.
“Parabéns, fulano, você já fez 18 anos!”'''

for i in range(1,21):
    nome = input(f"Informe o nome da {i}° pessoa: ")
    idade = int(input(f"Informe a idade da {i}° pessoa: "))
    if(idade >= 18):
        print(f"Parabéns, {nome}, você já fez 18 anos!")
