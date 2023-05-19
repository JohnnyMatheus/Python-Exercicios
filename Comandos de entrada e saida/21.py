#Faça um algoritmo que leia o ano em que uma pessoa nasceu, calcule e mostre a idade em anos,
# supondo que ela já fez aniversário nesse ano.

ano_Nascimento = int(input("Informe o ano do seu Nascimento: "))
ano_Atual = int(input("Informe o ano atual: "))
idade = ano_Atual - ano_Nascimento
print(f"Sua idade é {idade} anos")