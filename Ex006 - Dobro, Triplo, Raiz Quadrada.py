# Crie um algorítimo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada.

num = int(input('Me informe um número: '))
dobro = num * 2
triplo = (num* 3)
raiz = num ** 0.5
print('O dobro de {} é: {}\n'
      'O triplo de {} é: {}\n'
      'A raiz quadrada de {} é: {:.2f}\n'.format(num, dobro, num, triplo, num, raiz))
