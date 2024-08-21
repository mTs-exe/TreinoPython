# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o valor do ângulo: '))
radianos = math.radians(angulo) # É necessário converter o número para radianos, assim será possível fazer o cálculo
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print('O ângulo de {} tem o SENO {:.2f}'.format(radianos, seno))
print('O ângulo {} tem o COSSENO {:.2f}'.format(radianos, cosseno))
print('O ângulo {} tem a TANGENTE {:.2f}'.format(radianos, tangente))
