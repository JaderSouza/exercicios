from datetime import date
ano = int(input('Digite o ano para saber se ele é bissexto: (Coloque 0 para analisar o ano atual)'))
if ano == 0:
    ano = date.today().year #pega o ano atual configurado na maquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto contendo 366 dias.'.format(ano))
else:
    print('O ano {} não é um ano bissexto contendo 365 dias.'.format(ano))
