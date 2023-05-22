soma = 0
print("Informe a idade de 10 pessoas:")
cont = 1
while cont < 10+1:
    idade = int(input(f"Informe a idade da {cont}° pessoa: "))
    soma = soma + idade
    cont = cont + 1
print("A soma das idades é", soma)

