"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
"""
from math import pow,sqrt
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
print(f'Comprimento do cateto oposto: {catop:.2f}')
print(f'Comprimento do cateto adjacente: {catad:.2f}')
print(f'Comprimento da hipotenusa: {sqrt(pow(catop, 2) + pow(catad, 2)):.2f}')
"""
"""
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hip = (catop**2 + catad**2)**0.5
print(f'Comprimento do cateto oposto: {catop:.2f}')
print(f'Comprimento do cateto adjacente: {catad:.2f}')
print(f'Comprimento da hipotenusa: {hip:.2f}')
"""
from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(catop, catad)
print(f'Comprimento do cateto oposto: {catop:.2f}')
print(f'Comprimento do cateto adjacente: {catad:.2f}')
print(f'Comprimento da hipotenusa: {hip:.2f}')
