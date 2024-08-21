# Faça um algoritmo que leia o salário de um funcionário e mostre na tela o nmovo salário com um aumento de 15%
salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario * 15 /100
novo_salario = salario + aumento
print('O novo salario após o aumento de 15% vai ser de R${:.2f}!'.format(novo_salario))
