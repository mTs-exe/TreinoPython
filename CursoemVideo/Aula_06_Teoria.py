# Forma incorreta para somar, não está sendo definido como int()

''' n1 = input('Digite um número: ')
    n2 = input('Digite um número: ')
    soma = n1+n2
    print('A soma é', soma)'''

# Forma correta para somar.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
soma = n1+n2
print('A soma é', soma)

# Tipos de Dados
'''
Int(): São considerados inteiros como por exemplo, 7, -4, 0, 9875
Float(): São considerados números Reais como por exemplo, 4.5, 0.075, -15.640, 7.0
Bool(): São dados verificados como verdadeiro ou falso, True, False
str(): São strings, e são as palavras que ficam entre aspas, 'Olá', '7.5'
'''

# Saídas

print('a soma vale', soma)
print('A soma vale {}'.format(soma))
