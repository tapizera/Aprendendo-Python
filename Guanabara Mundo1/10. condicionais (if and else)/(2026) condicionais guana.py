print('~~~ 10. Condicionais ~~~')

#ex 28: adivinhar numero
from random import randint

pc = randint(1,5)
achoq = int(input('vou pensar num numero de 1 à 5, adinvha: '))
if achoq == pc:
    print('certou!')
else:
    print(f'errou! era {pc}')

#ex 29: 'radar eletronico', mas preferi esse de taxi
print('\n*vc é um motorista de táxi*')
percorreu = randint(0, 30)
print(f'andamo {percorreu}km e é 50 centavo por km')
tentaacertar = float(input('passageiro: quanto q deu aí a corrida?\nvc: '))
valordacurrida = percorreu * 0.5
if tentaacertar == valordacurrida:
    print('passageiro: blz, fiz aí o pix, valeu mano!')
else:
    print(f'passageiro: ei man tá errado isso aí ksks é {valordacurrida}')

#ex 31: custo da viagem (taxi 2)
distance = int(input('\ndistancia da viagem (só numero): '))
if distance <= 200:
    print(f'menos de 200km é R$0,50 o km, então deu R${distance * 0.5}')
else:
    print(f'mais de 200km é R$0,45 o km, então deu {distance * 0.45}')

#ex 32: ano bissexto
from datetime import date
ebissexto = int(input('\nque ano nos tamo?: '))

if ebissexto == date.today().year:
    if ebissexto % 4 == 0 and ebissexto % 100 != 0:
        print(f'o ano atual é bissexto')
    else:
        print(f'o ano atual não é bissexto')
elif ebissexto % 4 == 0 and ebissexto % 100 != 0:
    print(f'{ebissexto} é bissexto')
else:
    print(f'{ebissexto} não é bissexto')

#ex 33: menor e maior valor
a = int(input('\nnum1: '))
b = int(input('num2: '))
c = int(input('num3: '))
#a
if a<b and a<c:
    print(f'num1 {a} é o menor num')
elif a>b and a>c:
    print(f'num1 {a} é o maior num')
#b
elif b<a and b<c:
    print(f'num2 {b} é o menor num')
elif b>a and b>c:
    print(f'num2 {b} é o maior num')
#c
elif c<a and c<b:
    print(f'num3 {c} é o menor num')
else:
    print(f'num3 {c} é o maior num')

#ex 34: aumentos e decontos estacáveis
salario = int(input('\nvou aumentar teu salário! mas... tu ganha quanto?: '))
if salario <= 100:
    print('não pô ksksks toma aí +10.000%')
    print(f'*agora seu salário é {salario + (salario * 100)}*')
if salario > 100 and salario <= 1000:
    print('q isso tá pobre man ksks toma aí +200%')
    print(f'*agora seu salário é {salario + (salario * 3)}*')
if salario > 1000 and salario <= 3000:
    print('vish tá ganhando poquin, vou te dar +100%')
    print(f'*agora seu salário é {salario + (salario * 2)}*')
if salario > 3000 and salario <= 5000:
    print('ixi já tá de boa, toma aí +50%')
    print(f'*agora seu salário é {salario + 50/10}*')
if salario > 5000 and salario <= 10000:
    print('eita poxa tá ganhando q só a pora já ksksks toma aí +10%')
    print(f'*agora seu salário é {salario * 10/100}*')
if salario > 10000 and salario <= 100000:
    print('me dá')
    print(f'*vc foi roubado, agora seu salário é {salario - salario }*')
if salario > 100000:
    print('mintira')

#ex 35: analizer de trigulos v1 (???)
print('vamo criar um trigulo eeee')
r1 = float(input('1° segmento do trigulo: '))
r2 = float(input('2° segmento do trigulo: '))
r3 = float(input('3° segmento do trigulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('trigulo feito com sucesso')
else:
    print('vish, parece q n dá pra fazer trigulo com esses numero ai sla pq')