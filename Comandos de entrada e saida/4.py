'''Considere que se deseja desenvolver um algoritmo para calcular a quantidade
de azulejos que é necessário comprar para colocar em uma determinada parede.'''

larguraParede = float(input('Informe a largura da parede: '))
alturaParede = float(input('Informe a altura da parede: '))
largura_Azulejo = float(input("Informe a largura do azulejo: "))
altura_Azulejo = float(input("Informe a altura do azulejo: "))

area_parede = larguraParede * alturaParede
area_Azulejo = largura_Azulejo * altura_Azulejo
print(f"A area total da parede é = {area_parede}")
print(f"A area total da azulejo é = {area_Azulejo}")

Total = area_parede / area_Azulejo
print(f'É necessário comprar para colocar em uma determinada parede {Total} azulejo(s)')