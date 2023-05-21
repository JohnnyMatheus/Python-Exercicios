'''
Construir um algoritmo para verificar qual dos dois times foi o vencedor dos jogos do último final de semana.
Devem ser solicitados os nomes dos dois times e o número de gols realizados por cada um deles.
Ao final deve ser apresentado o resultado do jogo, com o vencedor, ou informando caso tenha havido um empate.

#############################################################
Exemplo 1 :  Internacional X Esportivo                      #
		        4		        1                           #
	        Resultado:   Internacional foi o vencedor       #
#############################################################
Exemplo 2 : Ypiranga X  Grêmio                              #
			   0	      0	                                #
 		     Resultado: Empate                              #
#############################################################
'''

timeA = str(input("Informe o nome do 1° time: "))
golsA = int(input("Informe o número de gols do 1° time: "))
timeB = str(input("Informe o nome do 2° time: "))
golsB = int(input("Informe o número de gols do 2° time: "))

if(golsA > golsB):
    print(f"{timeA}  x  {timeB}")
    print(f"{golsA}  X   {golsB}")
    print(f"Resultado: {timeA} foi vencedor")
elif(golsB > golsA):
    print(f"{timeA}  x  {timeB}")
    print(f"{golsA}  X   {golsB}")
    print(f"Resultado: {timeB} foi vencedor")
elif(golsA == golsB):
    print(f"{timeA}  x  {timeB}")
    print(f"{golsA}  x  {golsB}")
    print(f"Resultado: Empate")
else:
    print("Informe valores válidos")