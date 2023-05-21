'''Fazer um programa que leia 2 números inteiros em seguida apresente o seguinte menu. Se a opção escolhida
não for nenhuma das apresentadas, deve ser apresentada uma mensagem avisando que a opção é inválida.
	1 - Média entre os 2 números
	2 - Diferença do maior pelo menor – se forem diferentes
	3 – Sair (mostrar somente uma mensagem como Saindo... )

Obs: Lembrar de mostrar uma mensagem adequada caso o usuário digite um valor diferente de 1, 2 ou 3.'''

numero1 = int(input("Informe o 1° número: "))
numero2 = int(input("Informe o 2° número: "))
print("Escolha uma das opções abaixo: ")
print("1 - Média entre os 2 números\n"
      "2 - Diferença do maior pelo menor – se forem diferentes\n"
      "3 – Sair")
opcao = int(input("Informe a opção escolhida: "))

if(opcao == 1):
    print(f"A opção escolhida foi {opcao}")
    media = (numero1 + numero2)/2
    print(f"A média entre os números é = {media}")
elif(opcao == 2):
    print(f"A opção escolhida foi {opcao}")
    diferenca = numero1 - numero2
    print(f"A diferença entre {numero1} - {numero2} = {diferenca}")
elif(opcao == 3):
      print("Saindo...")
else:
    print("Valor inválido")
