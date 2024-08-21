# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância da viagem? '))
preco1 = 0.50
preco2 = 0.45
print('A distância que será percorrida em sua viagem é de {}Km.'.format(distancia))
if distancia <= 200:
    print('O valor de sua viagem ficou em R${:.2f}.'.format(distancia * preco1))
else:
    print('O valor de sua viagem ficou por R${:.2f}.'.format(distancia * preco2))
