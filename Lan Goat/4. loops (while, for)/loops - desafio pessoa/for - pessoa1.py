pessoa = {
    'nome':'davi',
    'idade':17,
    'cidade':'fortal'
}

for example in pessoa:
    print(f'nome:{pessoa['nome']}')

for chave, valores in pessoa.items():
    print(f'valores:{valores}')

for keys in pessoa.keys():
    print(f'chaves:{keys}')