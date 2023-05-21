'''Construir um algoritmo que calcule a média da disciplina de Laboratório de Prática de Algoritmos no semestre.
Considere que a avaliação A1 será composta por uma média ponderada da seguinte forma:
    #################################################
    #           Avaliação                 #   Peso  #
    #################################################
    #           Trabalho 1                #   25%   #
    #            Prova 1                  #   25%   #
    #            Prova 2                  #   30%   #
    #Trabalhos individuais e em duplas    #   10%   #
    #Atividades de ensino e extensão      #   10%   #
    #################################################

O programa deve solicitar a frequência do acadêmico. Após apresentar a média final,
o sistema deve informar uma mensagem com a situação do acadêmico dependendo de sua frequência e de suas notas, sendo:
Frequência mínima de 75% - aprovado, caso contrário reprovado.
7 a 10 – aprovado
menor que 4 – reprovado por média
entre 4 e 7 – em A2
'''

frequencia = int(input("Informe sua frenquência: "))
Trabalho1 = float(input("Informe a nota do Trabalho 1: "))
prova1 = float(input("Informe a nota da prova 1: "))
prova2 = float(input("Informe a nota da prova 3: "))
trabalhos_IndividuaisDuplas = float(input("Trabalhos individuais e em duplas: "))
AtividadeEXt = float(input("Informe a nota da  Atividade de ensino e extensão: "))

mediaPonderada = (Trabalho1 * 25 + prova1 * 25 + prova2 * 30 + trabalhos_IndividuaisDuplas * 10 + AtividadeEXt * 10)/100

if(mediaPonderada >= 7) and (mediaPonderada <= 10) and(frequencia >= 75):
    print(f"Aprovado - media = {mediaPonderada} e frequência = {frequencia}")
elif(mediaPonderada < 4):
    print("Reprovado por média")
elif(mediaPonderada >4) and(mediaPonderada < 7) and (frequencia > 75):
    print("Em A2")
else:
    print("Reprovado")