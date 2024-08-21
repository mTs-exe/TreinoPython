# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Informe a velocidade atual do carro: '))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print('MULTADO! A velocidade do carro foi excedida ao limite permitido de 80Km/h')
    print('o valor da multa para ser paga é R$ {:.2f}!'.format(float(multa)))
else:
    print('A velocidade está dentro do limite!')
print('Dirija com segurança! Tenha um bom dia!')
