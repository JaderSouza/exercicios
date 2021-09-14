print('=-='*20)
print('Analisando seguimentos para formar um triangulo')
print('=-='*20)
l1 = float(input('Digite o primeiro seguimento: '))
l2 = float(input('Dgite o segundo seguimento: '))
l3 = float(input('Digite o valor do terceiro seguimento: '))
# SIMPLIFICANDO OS IF'S (CONDIÇÕES).
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('os valores digitados podem formar um triangulo.')
else:
    print('os valores digitados não podem formar um triangulo.')    
#REPETINDO OS IF'S...
'''if l2 < l1 + l3:
    print('os valores digitado podem formar um triangulo.')
if l3 < l1 + l2:
    print('os valores digitado podem formar um triangulo.')
 if l1 < l2 + l3:
     print('os valores digitados não podem formar um triangulo.')   '''
print('=-='*20)    
