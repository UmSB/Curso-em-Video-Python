# Escreva um programa que leia o valor em metros e o exiba em centimetros e milimetros.
metro = float(input('Digite um valor em metros: '))
cm = metro * 100
mm = metro * 1000
print(f'O valor digitado em metros foi, {metro:.2f} m, convertendo para centimetros temos {cm:.2f} cm e para milimetros {mm:.2f} mm.')
