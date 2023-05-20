'''
O sistema de avaliação de determinada disciplina é composto por três provas.
A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5.
Considerando que a média para aprovação é 7.0. Construa um algoritmo para calcular a média final
de um aluno desta disciplina e dizer se o aluno foi aprovado ou não.
Lembre-se que essa é uma média ponderada e não uma média aritmética.
'''

pesoProva1 = 2
pesoProva2 = 3
pesoProva3 = 5

nota1 = float(input("Informe a nota da 1° Prova: "))
nota2 = float(input("Informe a nota da 2° Prova: "))
nota3 = float(input("Informe a nota da 3° Prova: "))
mediaPonderada = (pesoProva1 * nota1 + pesoProva2 * nota2 + pesoProva3 * nota3)/10

if(mediaPonderada >= 7):
    print(f"Aluno aprovado sua média é {mediaPonderada}")
else:
    print(f"Aluno reprovado sua média é {mediaPonderada}")
