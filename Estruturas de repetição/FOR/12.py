'''Escrever um programa que mostre os números múltiplos de 3 e de 5 existentes entre 301 e 401.
Os números múltiplos de 3 devem ser mostrados em azul e os múltiplos de 5 em amarelo.
Quando o número for múltiplo de 3 e de 5, ele deverá ser mostrado em rosa (purple).
Se não for múltiplo nem de 3 e nem de 5, deverá ser mostrada em branco. '''

class color:
    BLACK = '\33[30m'
    WHITE = '\33[40m'

    RED = '\33[91m'  # ou 31
    GREEN = '\033[92m'  # ou 32
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'

    BLACK_BACK = '\33[40m'
    RED_BACK = '\33[41m'
    GREEN_BACK = '\33[42m'
    YELLOW_BACK = '\33[43m'
    BLUE_BACK = '\33[44m'
    GRAY_BACK = '\33[47m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

for i in range(301,401 +1):
    if(i % 3 ==0):
        print(color.BLUE_BACK,i)
    elif(i % 5 == 0):
        print(color.YELLOW_BACK,i)
    elif(i % 3 == 0) and (i % 5 == 0):
        print(color.PURPLE,i)
    else:
        print(color.GREEN_BACK,i)



