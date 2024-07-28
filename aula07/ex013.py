"""
Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""
lar = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = lar * alt
print(f'Largura da parede: {lar:.2f}m')
print(f'Altura da parede: {alt:.2f}m') 
print(f'Aréa da parede: {area:.2f}m²')
print(f'Serão necessários {area/2:.2f} l de tinta para pintar toda a parede.')
