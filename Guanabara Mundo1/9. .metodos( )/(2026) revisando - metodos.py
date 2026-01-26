print("~~~ 9. Métodos ~~~")

# Metodos
exemplo = "exemplo"
len(exemplo)
exemplo.count('e')
exemplo.replace('x','z')
exemplo.upper()
exemplo.lower()
exemplo.capitalize() 
#1° letra maisculo e o resto minusculo
exemplo.title()
#primeiras letras maisculas
exemplo.strip()
#tira os espaços inúteis
exemplo.rstrip() #lstrip() (esquerda)
#tira os espaços da direita (right)
exemplo.split() #divisao
#La Ele (0123456) -> La Ele (01 012)
"s".join(exemplo)

#ex 22: upper, lower, split, count
nome = input("teu nome: ")
print(f"tudo maiuculo: {nome.upper()}")
print(f"tudo menuscuko: {nome.lower()}")
separido = nome.split()
print(f"q de digitos: {len(nome) - nome.count(' ')}")
print(f"{(separido[0])} tem {len(separido[0])} letras")

#ex 23: udcm
tuenumero = int(input('\n4 digitos: '))
u = tuenumero // 1 % 10
d = tuenumero // 10 % 10
c = tuenumero // 100 % 10
m = tuenumero // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

#ex 25: if bem la ele
print(f'\nTem Silva? - {'silva' in nome.lower()}')

#ex 26: 1ª e ultima letra
escreva = str(input('\nescreve palavras: ')).lower()
print(f'a letra A aparece {escreva.count('a')} vezes')
print(f'a 1° letra A aparece no {escreva.find('a')+1}° digito')
print(f'a ultima letra A aparece no {escreva.rfind('a')+1}° digito')

#ex 27: 1° e ultimo nome
iscreva = str(input('\nescreva nomes: '))
iscrevasplited = iscreva.split()
print(f'o primeiro nome é {iscrevasplited[0]}')
print(f'e o ultimo é {iscrevasplited[len(iscrevasplited)-1]}')