'''1.Supondo que a cotação do dólar para câmbio seja de R$5,00 e a cotação do Peso Argentino seja de R$0,20.
Quantos dólares e quantos pesos posso comparar com R$1214,00? Construa um programa com variáveis para calcular
a quantidade de pesos e de dólares que posso comprar.'''
Dolar = 5.00
pesos_Argentinos = 0.20
Real = 1214.00
qtd_Dolar = Real / Dolar
qtd_Pesos = Real / pesos_Argentinos

print(f"Será possível comprar US$ {qtd_Dolar:.2f} dolares ")
print((f"Sera possível comprar {qtd_Pesos} pesos Argentinos"))
