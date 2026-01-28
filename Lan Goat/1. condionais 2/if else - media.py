nome = str(input("qual teu nome? "))
nome2 = str(input('e sobrenome? '))
fullname = nome + ' ' + nome2
conhecido = {'davi','Davi','caua','Caua','cauã','Cauã','mateus','Mateus','matheus','Matheus'}

if nome in conhecido:
  print(f'{fullname}? acho q te conheço mas enfim')

else:
  print('ok')

serie_ok = {1,2,3,4,5,6,7,8,9}
serie = int(input('qual tua serie? '))
if serie in serie_ok:
  print('ok')
else:
  print('q raio de serie é essa?? da nao ksks')
  quit()

serie_string = str(serie)
fullserie = serie_string + str('° ano')

proxserie = serie + 1
proxserie_string = str(proxserie) + str('° ano')

print(f'pessoa {fullname} do {fullserie} cropitado com sucesso')

nota1 = float(input('qual tua primeira nota? '))
nota2 = float(input('qual tua segunda nota? '))
nota3 = float(input('qual tua terceira nota? '))
nota4 = float(input('qual tua quarta nota? '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media <= 5:
  print(f'ah q pena {fullname}, tu ficou com {media}, mas aproveite seu {fullserie} novamente')
elif media <= 9.9:
  print(f'parabens {fullname}, tu ficou com {media}, aproveite seu {proxserie_string}!')
elif media == 10:
  print(f'CARACA {fullname}, TU FICOU COM {media} DOIDO KSKS, agora é {proxserie_string} uhuuu!!')
else:
  print('mas oxi??? aí é la ele')

print('cropito de fim')