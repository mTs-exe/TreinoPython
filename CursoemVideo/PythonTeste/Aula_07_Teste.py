n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}\n '
      'A subtração é {}\n '
      'A multiplicação é {}\n '
      'A divisão é {:.3f}\n ' 
      'A divisão inteira é {}\n '
      'O expoente é {}. '.format(s, sub, m, d, di, e), end='')
print('Exemplos de operaçoes aritméticas')

# \n serve para que ocorra a quebra de linha, evitando que fique tudo na mesma linha
#Para não ocorrer a quebra de linha quando se tiver amis de um print(), utilize no final end=' '