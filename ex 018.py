import math
num = float(input('Digite um angulo qualquer em graus: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O seno de {:.2f} é igual a: {:.2f}.'.format(num, sen))
print('O cosseno de {:.2f} é igual a {:.2f}.'.format(num, cos))
print('A tangente de {:.2f} é igual a {:.2f}.'.format(num, tan))

