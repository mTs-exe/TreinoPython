# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

'''
import math
numero = float(input('Digite um número Real: '))
numero_inteiro = math.trunc(numero)
print('O número {} tem a parte inteira {}'.format(numero, numero_inteiro))

from math import trunc
numero = float(input('Digite um número: '))
print('O número {} tem como sua porção inteira {}'.format(numero, trunc(numero)))
'''

numero = float(input('Digite um número: '))
print('O número {} tem como sua porção inteira {}'.format(numero, int(numero)))
