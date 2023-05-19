'''Ana deseja fazer algumas comprinhas da Shopee e os produtos que ela deseja tem os seguintes valores:
bule de louça – US$ 25,00, alimentador automático para gatos – US$13,00.
O frete para esses dois produtos é de R$14,00.  Considerando que o valor da cotação do dólar é de R$5,00.
Qual será o valor total da compra de Ana em reais?
Se ela precisar pagar IOF de 6% sobre os produtos comprados, de quanto será o valor do imposto em reais?'''

bule = float(25.00)
alimentador = float(13.00)
frete = float(14.00)
dolar = float(5.00)
iof = 6/100

Valor_Reais = (bule + alimentador) * dolar
print(f'Valor em reais {Valor_Reais}')

Valor_Frete = Valor_Reais + frete
print(f"Valor dos Produtos com frete de R$14 reais: {Valor_Frete}")
imposto = (Valor_Frete*iof)/100
print(f"Imposto {imposto:.2f}")
valor_Total = Valor_Frete + imposto
print(f"O valor total dos produtos com imposto de 6% será de {valor_Total:.2f}")

