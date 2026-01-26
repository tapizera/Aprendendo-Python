numero_de_pedra = 0
valor_da_pedra = True
quantia = int(input('quantos deseja? '))

while valor_da_pedra:
  if numero_de_pedra < quantia:
     numero_de_pedra += 1 #mesma coisa que: numero_de_pedra = numero_de_pedra + 1
     print(numero_de_pedra)
  else:
    valor_da_pedra = False