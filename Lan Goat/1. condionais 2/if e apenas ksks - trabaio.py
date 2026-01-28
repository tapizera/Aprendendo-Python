nome = input("qual teu nome? ")
trabalho = input("quer trabaiar com que? ")
endereço = input("onde tu mora? ")
idade = int(input("qual tua idade? "))
resposta_sim = "sim";"s";"si";"pode ser"
resposta_nao = "não";"n";"no";"sla"

if idade < 18:
  print(f"ola {nome} do {endereço}, parece que vc tem {idade}, infelizmente vc é lá ele demais")

if idade >= 65:
  print(f"{nome} mancho, vai te aposentar man")

if idade >= 18 and idade < 65:
  input(f"ola {nome} do {endereço}, sua idade de {idade} é suficiente para {trabalho}, gostaria de aderir? ")
  if resposta_sim:
    print(f"entao ta, bem vindo {nome}, agora vc vai trabaiar com {trabalho}")
  if resposta_nao:
    print(f"entao ta, tchau tchau {nome}!")