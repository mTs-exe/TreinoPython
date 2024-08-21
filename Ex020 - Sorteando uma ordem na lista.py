# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
trabalho1 = str(input('Digite o nome do primeiro grupo: '))
trabalho2 = str(input('Digite o nome do segundo grupo: '))
trabalho3 = str(input('Digite o nome do terceiro grupo: '))
trabalho4 = str(input('Digite o nome do quarto grupo: '))
lista = [trabalho1, trabalho2, trabalho3, trabalho4]
random.shuffle(lista)
print('A ordem dos grupos que irão apresentar o trabalho é: {}'.format(lista))


