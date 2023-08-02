from random import choice
from time import sleep
n = [0, 1, 2, 3, 4, 5]
sorteado = choice(n)

print('-=-'*30)
num = int(input('Escolhi um numero de 0 a 5 adivinhe:'))
print('-=-'*30)

print('CARREGANDO...')
sleep(2)

if num == sorteado:
    print('Voce acertou o numero que escolhi!!!')
else:
    print('Voce falhou miseravelmente.')


