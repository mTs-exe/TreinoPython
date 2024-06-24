# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média entre as notas do aluno é {:.2f}'.format(media))
