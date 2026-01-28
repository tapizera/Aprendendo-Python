tupla0 = ('maçã', 'banana', 'uva', 'abacate')
print(tupla0.count('banana'))
#exibe quantas vezes o iten banana apareceu, no caso 1

tupla1 = ('maçã', 'banana', 'uva', 'abacate')
print(tupla1.index('maçã'))
#exibe a posição de maçã na lista, no caso 0
#count e index funcionam nas tuplas por n alterarem, só verificarem

tupla = ('maçã', 'banana', 'uva', 'abacate')
lista = list(tupla)
lista.append('pera')
tupla = tuple(lista)
print(tupla)
# FALSIFICAÇÃO DE TUPLA KSKSKSKS
#a tupla foi transformada em lista para adiconar pera e voltou a ser tupla