'''Considere a construção de um algoritmo que, leia a idade de uma pessoa e informe a sua faixa etária,
de acordo com a tabela a seguir:


      Classificação          Faixa etária
        Criança               até 12 anos
        Adolescente      maior de 12 e menor de 18
        Adulto                de 18 a 60 anos
        Idoso                 Mais de 60 anos
'''

idade = int(input("Informe sua idade: "))

if(idade <= 12):
    print("Criança")
elif(idade > 12) and (idade < 18):
    print("Adolescente")
elif(idade >= 18) and(idade <= 60):
    print("Adulto")
else:
    print("Idoso")
