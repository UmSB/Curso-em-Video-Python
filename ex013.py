"""
Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""
lar = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = lar * alt
print(f'A largura informada é {lar:.2f}m e a altura é {alt:.2f}m, logo a área da parede é {area:.2f}m². Serão necessários {area/2:.2f} l de tinta para pintar toda a parede.')
