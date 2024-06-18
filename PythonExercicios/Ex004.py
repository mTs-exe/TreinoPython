# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite qualquer coisa: ')
print('O tipo primitivo deste valor é:', type(n))
print('Esse valor só tem espaços?', n.isspace())
print('Esse valor é um número?', n.isnumeric())
print('Esse valor é alfabético?', n.isalpha())
print('Esse valor é decimal?', n.isdecimal())
print('Esse valor está em letras maiúsculas?', n.isupper())
print('Esse valor está em letras minúsculas?', n.islower())
print('Esse valor é alfanumérico?', n.isalnum())
print('Está capitalizada?', n.istitle())





