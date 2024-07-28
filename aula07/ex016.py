# Escreva um programa que converta uma temperatura digitada em °C para °F
temperaturaC = float(input('Digite a temperatura que quer converter: '))
temperaturaF = (temperaturaC * 9 / 5) + 32
temperaturK = temperaturaC + 273.5 
print(f'A temperatura é {temperaturaC:.2f} °C. Convertendo fica: ')
print(f'{temperaturaF:.2f} °F')
print(f'{temperaturK:.2f} K')


