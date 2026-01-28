numeros = ['1','2','3','4']
print(numeros)
numeros.insert(4,'6')
print(numeros)
numeros.remove('2')
print(numeros)
numeros.sort(reverse=True)
print(numeros)

print('desafio 1 concluido')

frutas_tupla = ('maçã','banana','laranja','uva')
print(f'{frutas_tupla[1]} está na lista') 
# o ideal seria:
# if 'banana' in frutas_tupla
#   print('banana ta nas fruta')

frutas_lista = list(frutas_tupla)
frutas_lista.append('abacaxi')
frutas_tupla = tuple(frutas_lista)
print(frutas_tupla)

print('desafio 2 concluido')

#pessoa = {'nome':'Maria','idade':'20','curso':'engenharia'}
#pessoa.append({'nota':'9.5'})
#pessoa['idade'] = '21'
#pessoa.remove(['curso'])
#cursos = ['mat','fis','logc']
#pessoa.append(['cursos'])
#print(pessoa)
# esse ta errado e o de baixo ta corrigido

aluno = {
    'nome':'fulano',
    'idade':'20',
    'curso':'pedreiro'
}
aluno['nota'] = 9.5
aluno['idade'] = 21
aluno.pop('curso')
aluno['cursos'] = ['fazendeiro', 'eletricista', 'agricultor']

print(aluno)