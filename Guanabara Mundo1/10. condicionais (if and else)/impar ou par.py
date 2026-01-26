import random
x = random.randint(0,11)
eu = ''
while True:
    eu = input('impar ou par?: ')
    if eu == 'impar':
        print('oponente: par')
        break
    elif eu == 'par':
        print('oponente: impar')
        break
    else:
        print('da não Man ksks')

n = int(input('meu número é: '))
if (n+x)%2 == 0 and eu == 'par':
    print(f'oponente: {x}')
    print(f'{n+x} é par, tu ganhou')
elif (n+x)%2 != 0 and eu == 'impar':
    print(f'oponente: {x}')
    print(f'{n+x} é impar, tu ganhou')
if (n+x)%2 == 0 and eu == 'impar':
    print(f'oponente: {x}')
    print(f'{n+x} é par, tu perdeu')
elif (n+x)%2 != 0 and eu == 'par':
    print(f'oponente: {x}')
    print(f'{n+x} é impar, tu perdeu')