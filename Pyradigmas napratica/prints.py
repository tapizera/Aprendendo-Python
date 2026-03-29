from datetime import datetime

str = 'Hello, World!'
print(str[::1]) #de 1 em 1
print(str[::-1]) #invertido
print(str[::2]) #de 2 em 2
# print(str[::0]) #erro, passo não pode ser 0
print(str[:5]) #do início até 4
print(str[7:13]) #World!
print(str[0]) #H, inxex 0 do conjunto de char (string)
print(str[-1]) #!, index -1

## hora formatada com datetime
hora = datetime.now().strftime("%H:%M:%S")
print(hora)
