# Crie um programa que leia quanto de dinheiro a pessoa tem na carteira e mostre quantos Dólares ela pode comprar

# Considere U$1,00 = R$5.46

real = float(input('Me diga quanto de dinheiro você tem na carteira: R$'))
dolar = real / 5.46
print('Com R${:.2f} é possível ter U${:.2f}!'.format(real, dolar))
