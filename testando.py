
i = 0
senha = input("Para continuar, digite sua senha: ")

while senha != 'a6b5c4':
    print("Senha inválida")
    i = i + 1
    senha = input("Para continuar, digite sua senha: ")

print("Seja bem-vindo(a) à área do cliente")
print(i)