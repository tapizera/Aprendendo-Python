pessoas = []

for i in range(3):
    nome = input('teu nome? ')
    nota = int(input('tua nota? '))
    comida = input('gosta de comer oq? ')
    pessoa = {'nome': nome, 'nota': nota, 'comida_favorita': comida}
    pessoas.append(pessoa)

for p in pessoas:
    print(f"olá {p['nome']}, vc tirou {p['nota']} e gosta de {p['comida_favorita']}")

# FEITA POR IA