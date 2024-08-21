# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco_semdesconto = float(input('Qual o preço do produto? R$ '))
desconto = preco_semdesconto * 5 / 100
preco_comdesconto = preco_semdesconto - desconto
print('O preço do produto com desconto é R$ {:.2f}!'.format(preco_comdesconto))
