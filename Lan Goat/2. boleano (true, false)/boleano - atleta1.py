idade = int(input('tua idade? '))

if idade >= 18:
  idade = True
else:
  idade = False

treina = True
quer = True

if idade and treina and quer == True:
  print('bem vindo/a')
else:
  print('lá ele')