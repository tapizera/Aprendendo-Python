print("~~~ 8. Modulos ~~~")

#ex 16: math.floor, math.ceil
import math
bota = float(input("bota ai decimal: "))
print(f"jabutado p cima: {math.ceil(bota)}")
print(f"jabutido p baixo: {math.floor(bota)}")

#ex 17: a soma dos quadrados...
co = float(input("\nteto oposot: "))
ca = float(input("teto acente: "))
hip = (ca ** 2 + co ** 2) ** (1/2)
print(f"hiponesua de {co} e {ca} é {hip}")
#ou
print(f"ou {math.hypot(co, ca)} também ")

#ex 18: seno conseno e senseno
xilito = float(input("\nbota o num p seno, conseno e tengente: "))
seno = math.cos(math.radians(xilito))
coseno = math.cos(math.radians(xilito))
tangente = math.tan(math.radians(xilito))
print(f"seno: {seno} \nconseno: {coseno} \ntemgente: {tangente}")

#ex 19: random.choice, random.radint
import random
tupla = ["Jucicreudo", "Jubileu", "Jucineide", "Julindo"]
choice = random.choice(tupla)
randint = random.randint(0, 1000)
print(f"\n{choice} ganhou {randint} conto")

#ex 20: random.shuffle
shuffle = random.shuffle(tupla)
print(f"top 4 melhores nomes:\n1- {tupla[0]}\n2- {tupla[1]}\n3- {tupla[2]}\n4- {tupla[3]}")

#ex 21: pygmame (nao funciona)
'''''''''''
import pygame
pygame.init()
pygame.mixer.load("ó a pancada.opus")
pygame.mixer.play()
pygame.event.wait()
'''''''''''