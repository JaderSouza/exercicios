from math import hypot
catoposto = float(input('Digite o valor do cateto oposto: '))
catadjacente = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(catoposto, catadjacente)
#hipot = (catoposto **2 + catadjacente **2)**0.5
print('A hipotenusa vai medir {:.2f}.'.format(hi))


