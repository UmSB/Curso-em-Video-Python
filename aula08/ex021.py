"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice
alum = input('Primeiro aluno: ')
aldois = input('Segundo aluno: ')
altres = input('Terceiro aluno: ')
alquat = input('Quarto aluno: ')
alunos = [alum, aldois, altres, alquat] # Lista: delimita-se por []
print(f'{choice(alunos)}') # O método choice() retorna um elemento selecionado aleatoriamente da sequência especificada
