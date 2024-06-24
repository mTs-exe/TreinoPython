# Faça um programa que leia um número Inteiro e mostre o seu sucessor e o seu antecessor

n = int(input('Me informe um número: '))
ant = n - 1
suc = n + 1
print('O número antecessor de {} é {}.\n'
      'O número sucessor de {} é {}.'.format(n, ant, n, suc))

print('O antecessor do número informado é {}, e o sucessor é {}.'.format((n-1), (n+1)))
