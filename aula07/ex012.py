# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
real = float(input('Quanto de dinheiro você possui: R$ '))
dolar = 5.57 # Valor de contação atual
print(f'Você possui R$ {real:.2f} reais e o dolar custa R$ {dolar:.2f} reais, logo, você pode comprar US$ {(real / dolar):.2f} dolares.')
