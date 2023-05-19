#Faça um algoritmo que leia o peso de uma pessoa em kg e mostre esse peso em gramas
# (lembre de formatar o número real)

gramas = float(1000)
kg = float(input("Informe seu peso: "))
peso = kg * gramas
print(f"O peso {kg} KG convertido para G = {peso:.2f} gramas")