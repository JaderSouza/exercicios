from random import choice
#import random
nome1 = input('digite o primeiro nome: ')
nome2 = input('digite o segundo nome: ')
nome3 = input('digite o terceiro nome: ')
nome4 = input('digite o quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista)
print('O aluno escolhido foi: {}'.format(sorteio))
