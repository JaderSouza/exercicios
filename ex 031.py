dist = float(input('Digite a distância da viagem em kms: '))
if dist <= 200:
    dist  = dist * 0.50
    print('Sua viagem vai custar {:.2f} reais.'.format(dist))
else:
    dist = dist * 0.45
    print('Sua viagem vai custar {:.2f} reais.'.format(dist))
