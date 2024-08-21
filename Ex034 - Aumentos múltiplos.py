# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o valor do salário? R$ '))
aumento10 = salario + (salario * 10/100)
aumento15 = salario + (salario * 15/100)
if salario <= 1250:
    print('O novo salário será R$ {:.2f}'.format(aumento15))
if salario > 1250:
    print('O novo salário será R$ {:.2f}'.format(aumento10))
print('Parabéns pelo aumento em seu salário!')
