idade = 18
quer = True
pode = False

if idade >= 18 and ((quer or pode) or (quer and pode)):
  print('bem vindo')
else:
  print('lá ele')