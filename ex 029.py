km = float(input('digite a sua velocidade em km/h: '))
if km > 80:
    print('MULTADO!! Você excedeu a velocidade regulamentada de 80kms/h.')
    print('Você estava {}kms/h acima da velocidade permitida. Sua multa será de {:.2f} reais'.format(km - 80, (km - 80) * 7))
else:
    print('Parabens, você estava dentro da velocidade regulamentada. Continue assim...')


