'''Elabore um algoritmo para testar se uma senha digitada é igual a “Patinho Feio”.
Se a senha estiver correta mostre a mensagem “Acesso permitido”,
do contrário mostre a mensagem “Você não tem acesso ao sistema”.
'''

senha = str(input("Informe a senha: "))

if(senha == 'Patinho Feio'):
    print("Acesso permitido")
else:
    print("Você não tem acesso ao sistema")