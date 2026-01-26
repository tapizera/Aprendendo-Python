pessoas = []

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    comida = input('Comida favorita: ')
    pessoa = {'nome': nome, 'idade': idade, 'comida_favorita': comida}
    pessoas.append(pessoa)
    continuar = input('Deseja cadastrar outra pessoa? (s/n): ').strip().lower()
    if continuar != 's':
        break

# 1. Quantas pessoas foram cadastradas
print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')

# 2. Média de idade
if pessoas:
    media_idade = sum(p['idade'] for p in pessoas) / len(pessoas)
    print(f'Média de idade: {media_idade:.2f}') #:.2f -> formatação p decimal dps da virgula só ter 2 digitos
else:
    print('Nenhuma pessoa cadastrada para calcular média de idade.')

# 3. Lista de quem gosta de pizza
pizza_lovers = [p['nome'] for p in pessoas if p['comida_favorita'].lower() == 'pizza']
print('Pessoas que gostam de pizza:', ', '.join(pizza_lovers) if pizza_lovers else 'Ninguém')