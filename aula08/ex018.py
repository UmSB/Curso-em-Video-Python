# Crie um programa que leia um número Real qualquer pelo teclado e mostre ne tela sua porção Inteira.
"""
from math import trunc
num = float(input('Digite um número: '))
print(f'A parte inteira do número {num} é {trunc(num)}')
"""
num = float(input('Digite um número: '))
print(f'A parte inteira do número {num} é {int(num)}')
