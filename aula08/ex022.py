"""
Um professor quer sortar a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
sorteio = [al1, al2, al3, al4]
shuffle(sorteio)
print(f'A ordem sorteada é: ')
print(sorteio)
