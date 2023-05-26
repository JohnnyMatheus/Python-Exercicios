import random
soma = 0
maior = 0
for cont in range(20):
    x = random.randint(1,50)
    print(x, end=' ')
    soma = soma +x
    if(x % 2 == 0):
        maior = x
    media = soma/20
print('\n')
print(f'Soma = {soma}\n'
      f'Par = {maior}\n'
      f'Media {media:.2f}')