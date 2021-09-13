nome = str(input('Digite um nome completo: ')).strip()
print('O seu nome com todas as letras maiúsculas fica {}:'.format(nome.upper()))
print('O seu nome com todas as letras minusculas fica {}:'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))

