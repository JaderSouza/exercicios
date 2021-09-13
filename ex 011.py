largura = float(input('digite a largura em metros:'))
altura  = float(input('digite a altura em metros:'))
A = largura * altura
tinta = A / 2
print('A sua parede tem a dimensão {:.2f}x{:.2f} e sua area é igual a {:.2f}m²'.format(largura, altura, A))
print('você precisara de {} litros de tinta para pintar essa parede.'.format(tinta))
