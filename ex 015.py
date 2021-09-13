quantKM = float(input('Digite em a quantidade de kilometros percorridos:'))
quantDIAS = float(input('Por quantos dias o carro foi alugado'))
aluguel = (quantDIAS * 60) + (quantKM * 0.15)
print(' O preço de aluguel a ser pago pelo veiculo que percorreu {:.2f}kms e foi alugado por {:.2f} dias custará {:.2f}R$'.format(quantKM, quantDIAS, aluguel))
