# Métodos de teste de tipo
# Métodos isnumeric() diz se é possivel converter o valor em um número primitivo int
# Métodos isalpha() se é alfa (alfabetico, letra)
# Métodos isalnum() se é alfanumérico
# Métodos isupper() se todas as letras são maiúsculas
# Métodos isupper() se todas as letras são minusculas
# Métodos istitle() True se todas as palavras em um texto começam com uma letra maiúscula e o restante da palavra são letras minúsculas
# Métodos isspace() se só tem espaço

algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Só tem espaço? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está em minusculo? {algo.islower()}')
print(f'Está capitalizado? {algo.istitle()}')
