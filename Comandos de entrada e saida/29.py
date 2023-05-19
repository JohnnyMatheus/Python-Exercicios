'''
Construir um programa que solicite ao usuário um valor em Reais, calcule e mostre esse valor convertido em:
- Pesos Argentinos
- Pesos Uruguaios
- Pesos Chilenos
- Dólares Americanos
- Euros

Utilizar Taxas de Câmbio oficiais do Banco Central do Brasil.
'''
pesos_Argentinos = float(0.021)
pesos_Uruguaios = float(0.13)
pesos_Chilenos = float(0.0063)
dolares_Americanos = float(5.00)
Euros = float(5.40)

Real = float(input("Informe o valor em Reais a ser convertido: "))
pesos_Argentinos =Real / pesos_Argentinos
pesos_Uruguaios = Real / pesos_Uruguaios
pesos_Chilenos = Real / pesos_Chilenos
dolares_Americanos = Real / dolares_Americanos
Euros = Real / Euros

print(f"O valor R$ {Real} reais\n"
      f"Pesos Argentinos {pesos_Argentinos:.2f}\n"
      f"Pesos Uruguaios {pesos_Uruguaios:.2f}\n"
      f"Pesos Chilenos {pesos_Chilenos:.2f}\n"
      f"Dólares Americanos {dolares_Americanos:.2f}\n"
      f"Euros {Euros:.2f}")

