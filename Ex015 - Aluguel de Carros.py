# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado ea quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e
# R$ 0.15 por km rodado

dias_alugados = int(input('Quantos dias o carro foi alugado? '))
KM_rodados = float(input('Quantos km foram rodados? '))
preco_aluguel = (dias_alugados * 60) + (KM_rodados * 0.15)
print('O preço a pagar pelo aluguel do carro é R${:.2f}'.format(preco_aluguel))
