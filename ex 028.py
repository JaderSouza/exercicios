from random import randint
from time import sleep
print('-=-'*12)
print('Jogo da advinhação')
print('-=-'*12)
num = int(input('Será que você consegue advinhar o número que eu escolhi??? Digite um número inteiro entre 0 e 5'))
numPC = randint(0 , 5)
print('PROCESSANDO...')
sleep(5)
if num == numPC:
    print('Parabens você me venceu!! O número era {}'.format(numPC))
else:
    print('Ganhei!! Pensei no número: {}, tente novamente.'.format(numPC))
print('-=-'*12)
sleep(10)
