import builtins
import time
println = builtins.print
ValHora = float(input('qual o valor da sua hora de trabalho?'))
HoraTrab = float(input('quantas horas você trabalhou esse mês?'))
Salario = ValHora * HoraTrab
Ir = Salario * 0.11
Inss = Salario * 0.08
Sindicato = Salario * 0.05
SalarioLiq = Salario - Ir - Inss - Sindicato
"""println(
'+ Salário Bruto : {}R$\n'
'- IR (11%) : {}R$\n'
'- INSS (8%) : {}R$\n'
'- Sindicato ( 5%) : {}R$\n'
'= Salário Liquido : {}R$\n'.format(Salario, Ir, Inss, Sindicato, SalarioLiq))"""
print('+ Salário Bruto : {}R$'.format(Salario))
print('- IR (11%) : {}R$'.format(Ir))
print('- INSS (8%) : {}R$'.format(Inss))
print('- Sindicato ( 5%) : {}R$'.format(Sindicato))
print('= Salário Liquido : {}R$'.format(SalarioLiq))
