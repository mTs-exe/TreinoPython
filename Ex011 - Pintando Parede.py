'''
Faça um programa que leia a largura e altura de uma parece em metros, calcule a sua área e a quantidade de tinta
necessária para pintar, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
'''

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
Quantidade_Tinta = area / 2
print('Com a parede tendo {:.2f} metros de largura e {:.2f} metros de altura sua área equivale a {:.2f} '
      'metros quadrados.\n'
      'Para pintar toda a parede será necessário {:.1f} litros de tinta'.format(largura, altura, area,
                                                                                Quantidade_Tinta))
