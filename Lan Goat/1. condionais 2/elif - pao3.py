pao = 2

r = input('ola bom dia, quer pao? ')

if r == str('s') and str('sim') and str('pode ser'):
  money = int(input('um pao ta 2 conto, tem quanto ai? '))
else:
  print('lá ele entao')
  quit()

multi_pao = pao*money

if money > 2:
  print(f'então vou te dar {multi_pao} pao')

if money == 2:
  print(f'então toma 1 pao ksks')

elif money < 2:
  print(f'aff probe, vo te dar pao de graça ent')