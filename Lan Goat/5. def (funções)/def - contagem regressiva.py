
# oq eu fiz e o lan tmb
def contagem_regressiva():
    resposta = int(input('1. bota ai um numero: '))

    while True:
        resposta -= 1
        print(resposta)
        if resposta <= 0:
            break

contagem_regressiva()

# oq o lan recomendou dps, sem precisar do if
def ctg_reg2():
    resposta = int(input('2. bota ai um numero: '))

    while resposta >= 1:
        resposta -= 1
        print(resposta)

ctg_reg2()

# usando for
def ctg_reg3():
    resposta = int(input('3. bota ai um numero: '))

    for i in range(resposta, -1, -1):
        print(i)

ctg_reg3()