i = int(input('ola, procuramos atleta, qual tua idade? '))

if i >= 18:
  i = True
else:
  i = False
  print('la ele')
  quit()

t = str(input('treina? '))

if t == str('s'):
  t = True
else:
  t = False
  print('la ele')
  quit()

d = str(input('tem deficiencia? '))

if d == str('n'):
  d = True
else:
  d = False
  print('la ele')
  quit()

if i and t and d == True:
  print('blz, bem vindo entao!')
else:
  print('lá ele')