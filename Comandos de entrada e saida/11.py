#Criar um algoritmo que solicita ao usuário uma letra e depois mostra essa letra informada.

lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
letra = str.lower(input("Informe uma letra: "))

if(letra in lista):
    print(f"A letra informada foi : {letra}")
else:
    print("ERRO")