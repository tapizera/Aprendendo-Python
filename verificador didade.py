from datetime import datetime, date

selecione = int(input('1-escola\n2-jovem aprendiz \n3-estágio\n4-trabalho\n5-aposentadoria\n\n> selecione: '))
dia = int(input('qual dia do teu aniversario?: '))
mes = int(input('mes?: '))
ano = int(input('ano?: '))
birth = date(ano, mes, dia)
hoje = date.today()
idade = hoje.year - birth.year

# se nao chegou no aniversario desse ano entao nao conta
if (hoje.month, hoje.day) < (birth.month, birth.day):
    idade -= 1

# verificando
if selecione == 1:
    if idade < 18:
        print('ok, pode ir')
    else:
        print('pode nao man ks')

elif selecione == 2:
    if idade == 16 or idade == 17:
        print('ok, pode ir')
    else: 
        print('pode nao man ks')

elif selecione == 3:
    if idade >= 18 and idade <= 20:
        print('ok, pode ir')
    elif idade > 20:
        print('vai trabaiar q é milho')
    else:
        print('muito novo vai p escola')

elif selecione == 4:
    if idade >= 18 and idade <= 64:
        print('ok, pode ir')
    elif idade > 64:
        print('vai aposentar q é milho')
    elif idade >= 18 and idade <= 20:
        print('tá novin, faz estágio q é milho')
    elif idade >= 16 and idade <= 18 :
        print('muito novo faz jovem aprendiz q é milho')
    else:
        print('muito novo vai p escola')

elif selecione == 5:
    if idade >= 65:
        print('ok, pode ir')
    elif idade >= 18 and idade <= 64:
        print('pode nao man ks')
    elif idade >= 18 and idade <= 20:
        print('pode nao man ks')
    elif idade >= 16 and idade <= 18 :
        print('pode nao man ks')
    else:
        print('muito novo vai p escola')