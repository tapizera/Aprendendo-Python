print('~~~ 7. Basico ~~~ ')

#ex 5
n = int(input('bota um número: '))
print('antecessor:',n-1)
print('sucessor:',n+1)

#ex 6
n = int(input('bota um número: '))
print('dobro:',n*2)
print('triplo:',n*3)
print('raiz:', n**(1/2))

#ex 7
n1 = int(input('nota 1: '))
n2 = int(input('nota 2: '))
ns = [n1, n2]
print('tua média é:',(n1+n2)/(len(ns)))

#ex 8
n = int(input('bota um numero ai: '))
print(n,'metros =',n*100,'cm =',n*1000,'mm')

#ex 9
n = int(input('bota um numero ai: '))
for v in range(11):
  print(f'{n} x {v} = {n*v}')

#ex 10
r = float(input('tem quantos reais aí?: '))
print(f'esses teus {r} reais = {r*0.19} dólares')
d = float(input('tem quantos dolares aí?: '))
print(f'esses teus {d} dólares = {d*5.4} reais')

#ex 11
l = float(input('largura da tua parede: '))
c = float(input('comprimento da tua parede: '))
print(f'a área da tua parede é: {l*c}')
print(f'cada litro de tinta pinta é 2m²,\nvc precisa de {(l*c)//2}')
t = float(input('tem quantos litro aí?: '))
if t > l*c//2:
  print('vc pode pintar sua parede')
else:
  print('nao da pra pintar a parede ainda')

#ex 12
print('Eu: qual o preço desse protuto?')
produto = float(input('Trabaiador: o preço q tu quiser man, diz um número aí: '))
print(f'Trabaidor: nah, vou dar 5% de desconto,\nentão fica R$',produto - (produto/20))
quer = str(input('(voz do além: agradeçe o cara)\nEu: '))
print('valeu man até a próxima!')

#ex 13
r = input('olá, vc gostaria de trabalhar aqui?(s/n): ')
if r == "s":
  print('o salário aqui é R$10.000')
  nome = str(input('qual teu nome mesmo?: '))
  print('MENTIRA VEI, n te reconheci, se quiser ficar, teu salário vai ser R$10.000 base')
  print('MAS... vou aumentar 10% cada mês')
  chute = input('então no 2° mês teu salário é: ')
  if chute == "11" and "11 mil" and "11k" and "11.000" and "11,000" and "11mil" and "11000":
    print('isso! contratado')
  else:
    print('demitido ksks')
else:
  print("ah, ta bom")

#ex 14
p = 10
print('produto tá 10 reais\ne c 15% de desconto\nvalor ficou: R$',10-((10/10)+(10/20)))

#ex 15
temp = float(input('quantos °C aí?: '))
print(f'sabia q {temp}°C é = {temp*1.8+32}°F?')
print(f'e também q {temp}°C é = {temp+273.15}K?')