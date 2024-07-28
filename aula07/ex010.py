# Escreva um programa que leia o valor em metros e o exiba em centimetros e milimetros.
metro = float(input('Digite um valor em metros: '))
km = metro * 0.001
hm = metro * 0.01
dam = metro * 0.1
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'O valor {metro:.4f}m corresponde há: ')
print(f'{km:.4f}km;')
print(f'{hm:.4f}hm;')
print(f'{dam:.4f}dam;')
print(f'{dm:.4f}dm;')
print(f'{cm:.4f}cm;')
print(f'{mm:.4f}mm.')
