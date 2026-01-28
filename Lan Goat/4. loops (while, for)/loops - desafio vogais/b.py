def achar_vogais(str):
    contador = 0
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for l in str:
        if l in vogais:
            contador += 1
        else:
            continue
    print(f'essa string maneira tem {contador} vogal(is)')
    
str_maneira = input('palavra maneira: ')
print(achar_vogais(str_maneira))