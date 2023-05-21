'''Pedir a nora de 5 alunos calcular e mostrar a média'''
for i in range(1,5+1):
    nota1 = float(input(f"Informe a 1° nota  do {i}° aluno: "))
    nota2 = float(input(f"Informe a 2° nota  do {i}° aluno: "))
    media = (nota1 + nota2)/2
    print(f"A media do {i}° aluno é {media}")