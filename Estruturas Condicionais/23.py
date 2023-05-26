x1 = int(input("Digite um número positivo: "))
x2 = int(input("Digite outro número positivo: "))

if(x1>x2):
    res = (x1 - x2)/x1
else:
    res = (x2 - x1)/x2

print(res)