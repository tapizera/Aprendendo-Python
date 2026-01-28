lista0 = ['maçã', 'banana?', 'uva']
print(lista0)
#exibe maçã, banana, uva

lista1 = ['maçã', 'banana', 'uva']
print(lista1[1])
#exibe banana por causa do index

lista2 = ['maçã', 'banana', 'uva', 'abacate']
print(lista2[:1])
#exibe maçã

lista3 = ['maçã', 'banana', 'uva', 'abacate']
print(lista3[0:2])
#exibe maçã, banana

lista4 = ['maçã', 'banana', 'uva', 'abacate']
print(len(lista4))
#exibe a quantidade de itens na lista, no caso 4

lista5 = ['maçã', 'banana', 'uva', 'abacate']
print(lista5.count('banana'))
#exibe quantas vezes o iten banana apareceu, no caso 1

lista6 = ['maçã', 'banana', 'uva', 'abacate']
print(lista6.index('maçã'))
#exibe a posição de maçã na lista, no caso 0

lista7 = ['maçã', 'banana', 'uva', 'abacate']
lista7.append('pera')
print(lista7)
#adiciona pera na lista e exibe

lista8 = ['maçã', 'banana', 'uva', 'abacate']
lista8.insert(0,'pera')
print(lista8)
#adiciona pera na lista na 1° posição (pelo 0 do index) e exibe

lista9 = ['maçã', 'banana', 'uva', 'abacate']
lista9.remove('maçã')
print(lista9)
#remove maçã da lista exibe

lista10 = ['maçã', 'banana', 'uva', 'abacate']
lista10.pop(0)
print(f'lista 10 é {lista10}')
#remove maçã da lista e exibe a lista sem a maçã

lista11 = ['maçã', 'banana', 'uva', 'abacate']
print(f'lista 11 é {lista11.pop(0)}')
#exibe o que removeu, no caso a maçã

lista12 = ['maçã', 'banana', 'uva', 'abacate']
lista12.clear()
print(lista12)
#exibe a lista limpa

lista13 = ['maçã', 'banana', 'uva', 'abacate']
lista13_copia = lista13
lista13.remove('abacate')
print(lista13)
print(lista13_copia)
#exibe as 2 listas idênticas, mesmo sem remover abacate da copia
#pq a lista13 e lista13_copia são assimiladas ocupando o mesmo canto na memoria

lista14 = ['maçã', 'banana', 'uva', 'abacate']
lista14_copia = lista14.copy()
lista14.remove('abacate')
print(lista14)
print(lista14_copia)
#agora exibe duas listas diferentes, pq uma é cópia

lista15 = ['maçã', 'banana', 'uva', 'abacate']
lista15.sort()
print(lista15)
#exibe a lista em ordem alfabetica: abacate, banana, maçã, uva

lista16 = ['maçã', 'banana', 'uva', 'abacate']
lista16.sort(reverse=True)
print(lista16)
#exibe a lista em ordem alfabetica reversa