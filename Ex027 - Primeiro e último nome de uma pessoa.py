# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Prazer em te conhecer!'
      ' Seu Primeiro nome é {}'
      ' e seu último nome é {}'.format(nome[0], nome[len(nome)-1]))
