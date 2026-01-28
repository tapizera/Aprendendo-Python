frase = input('escreve uma coisa aí: ')
quantia_vogais = 1
vogais = ["a", "e", "i", "o", "u"]

for i in vogais:
        if quantia_vogais == 1:
            print(f'{frase} tem {quantia_vogais} vogal')
        if quantia_vogais != 1:
             print(f'{frase} tem {quantia_vogais} vogais')
             quantia_vogais += 1
        else:
            print(f'{frase} nao tem nenhuma vogal')