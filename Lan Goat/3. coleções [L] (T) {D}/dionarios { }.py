pessoa = {'nome':'davi', 'idade':'17', 'cidade':'fortal'}
print(pessoa.get('nome', 'sei nao'))
#exibe o (valor) davi como (chave) nome
#caso nao encontre - exibe sei nao

pessoa = {'nome':'davi', 'idade':'17', 'cidade':'fortal'}
pessoa['cidade'] = 'caninde'
print(pessoa)
#trocou (valor) fortal por (valor) caninde da (chave) cidade