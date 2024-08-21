# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
print('Informe abaixo o segmento de 3 retas e veremos se elas podem formar um triângulo.')
m1 = float(input('Primeiro segmento: '))
m2 = float(input('Segundo segmento: '))
m3 = float(input('Terceiro segmento: '))

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    '''
    Para que seja formado um triângulo o valor de cada segmento
    Deve ser menor que a soma dos outros 2 valores
    '''
    print('Os segmentos informados PODEM formar um triângulo.')
else:
    print('Os segmentos escolhidos NÃO PODEM formar um triângulo.')

