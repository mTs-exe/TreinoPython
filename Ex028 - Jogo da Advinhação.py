# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
num = random.randint(1, 5)
nome = str(input('Olá, qual o seu nome? ').capitalize().strip())
print('É um prazer conhecer você {}! Vamos jogar um jogo!'.format(nome))
sleep(1)
print('Irei pensar em um número entre 1 e 5 e você tenta adivinhar.')
sleep(2)
num_jogador = str(input('Em que número estou pensando? '))
print('CARREGANDO...')
sleep(3)
if num == num_jogador:
    print('Parabéns você ganhou, eu estava pensando no número {}'.format(num))
else:
    print('Que pena, você errou, eu estava pensando no número {}!'.format(num))
