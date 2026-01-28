nome = str(input('Qual seu nome? '))
idade = int(input('Quantos ano vc tem? '))
cidade = input('E onde vc mora? ')

pessoa = {
    'nome_chave':{nome},
    'idade_chave':{idade},
    'cidade_chave':{cidade}}

print(f'seu nome é {[nome]}')