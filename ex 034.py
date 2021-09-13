print('=-='*15)
print('Calculando o Aumento do Salário.')
print('=-='*15)

sal = float(input('Digite seu salário em reais: '))
#verificação
if sal <= 1250:
    sal = sal + sal * 0.15
    print('Seu salário atual é igual a {}'.format(sal))
else:
    sal = sal + sal * 0.10
    print('Seu salário atual é igual a {}'.format(sal))

print('=-='*15)
