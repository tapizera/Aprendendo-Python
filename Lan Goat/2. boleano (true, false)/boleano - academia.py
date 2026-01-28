i = int(input('quantos ano? '))
if i >= 18:
  i = True
else:
  i = False
  print('lá ele')
  quit()

t = input('quer treina? ')
if t == str('s') and str('sim') and str('si'):
  t = True
else:
  t = False
  print('mas...')

m = input('medico mandou? ')
if m == str('s') and str('sim') and str('si'):
  m = True
else:
  m = False
  print('mas...')


if i and (t or m) == True:
  print('bem vindo')
else:
  print('lá ele total')