multi = 1
pedido = int(input('bota um número aí: '))

for num in range(1, 11):
    result = pedido*multi
    print(f'{pedido} x {num} = {result}')
    multi += 1 # nao precisava