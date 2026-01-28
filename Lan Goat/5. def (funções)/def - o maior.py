
# o maior da lista q o lan fez
def maior(lista):
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior

lista = [5, 1, 3, 10, 8]
maior_da_lista = maior(lista)
# print(f'o maior daí é {maior_da_lista}')

# ou...
# o maior da lista usando max
def maior(lista):
    maior = max(lista)
    return maior

lista = [5, 1, 3, 10, 8]
maior_da_lista = maior(lista)
print(f'o maior daí é {maior_da_lista}')