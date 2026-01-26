import random

nomes = []
for i in range(4):
    nome = input(f'Digite o nome {i+1}: ')
    nomes.append(nome)

random.shuffle(nomes)

print
for i, nome in enumerate(nomes, start=1):
    print(f'{i}°: {nome}')