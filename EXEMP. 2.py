#import math
Metro = float(input('Digite a superficie em metros quadrados:'))
ValorTinta = 80
Rendimento = 54
#QuantLatas = math.ceil(Metro / Rendimento)
QuantLatas = float(Metro / Rendimento)
quantlantasInt = Metro // Rendimento
restoLatas = Metro % Rendimento
print(restoLatas)
print(quantlantasInt)

if QuantLatas - quantlantasInt > 0:
    quantlantasInt += 1 



print('A quantidade de latas será {}, e o valor gasto será {}R$'.format(quantlantasInt, quantlantasInt * ValorTinta))


