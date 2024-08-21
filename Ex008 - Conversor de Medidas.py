# Escreva um programa que lei aum valor em metros e o exiba convertido em centímetros e milímetros

medida_metros = float(input('Me informe uma medida em metros: '))
centimetros = medida_metros * 100
milimetros = medida_metros * 1000
print('A medida de {} em centímetros é {:.1f} e em milímetros é {:.1f}'.format(medida_metros, centimetros, milimetros))
