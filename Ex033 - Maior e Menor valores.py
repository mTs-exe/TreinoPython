# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero1 = int(input('Digite um número qualquer: '))
numero2 = int(input('Digite mais um número qualquer: '))
numero3 = int(input('Só mais um número: '))
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
maior = numero2
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print('O primeiro valor foi: {}'.format(numero1))
print('O segundo valor foi: {}'.format(numero2))
print('O terceiro valor foi: {}'.format(numero3))
print('O menor valor é o número {}'.format(menor))
print('O maior valor é o número {}'.format(maior))
