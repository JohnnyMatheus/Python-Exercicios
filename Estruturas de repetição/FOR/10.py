'''Escrever um programa que mostre a frase “1, 2, 3 ... testando” em linhas diferentes 30 vezes.
As linhas ímpares devem ser vermelhas e as linhas pares devem ser verdes. '''


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


for i in range(1,31):
    if(i % 2 ==0):
        print(color.RED_BACK + "1, 2, 3 ... testando",i)
    else:
        print(color.GREEN_BACK+"1, 2, 3 ... testando", i)
