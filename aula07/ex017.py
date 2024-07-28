"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 reais por dia e R$ 0,15 reais por km rodado.
"""
diasalug = int(input('Quantidade dias de aluguel: '))
kmalug = float(input('Quantidade de km percorridos: '))
valordias = diasalug * 60
valorkm = kmalug * 0.15
valortot = valorkm + valordias
print(f'O carro foi alugado por {diasalug} dias e percorreu {kmalug:.2f} km. O valor total do aluguel é R$ {valortot:.2f} reais.')
