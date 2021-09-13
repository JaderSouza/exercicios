from time import sleep
print('-=-'*15)
print('Vamos saber quaal foi o maior e o menor número digitados?')
print('-=-'*15)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o  terceiro número: '))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
'''else: 
    print('Você digitou o mesmo número três vezes!!')'''
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))                       
print('-=-'*15)
sleep(5)


