# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente

"""
from math import radians, sin, cos, tan # Valores de sin, cos e tan vem em radianos
valor = float(input('Digite o valor desejado: '))
valconv = radians(valor)
print(f'O angulo de {valor:.2f} tem seno de {cos(valconv):.2f}')
print(f'O angulo de {valor:.2f} tem cosseno de {cos(valconv):.2f}')
print(f'O angulo de {valor:.2f} tem tangente de {tan(valconv):.2f}')
"""
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo:.2f} tem o seno de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo:.2f} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo:.2f} tem a tangente de {tangente:.2f}')
