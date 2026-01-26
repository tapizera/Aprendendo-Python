import random
count = 0     
count2 = 0
lista = ['cara', 'coroa']
coin = random.choice(lista)
while True:
    chute = input('💿 cara ou coroa: ')
    if coin == chute:
        print(f'💥 {coin}')
        print('✔️  acertou')
        count += 1
        print(f'😎 you: {count}, 👾 opponent: {count2}')
        again = input('🔄 quer ir dnv?(s/n): ')
        if again == 's':
            coin = random.choice(lista)
            continue
        else:
            print('👍 ta bom tchau')
            if count > count2:
                print(f'😎 you: {count} WINNER 🏆, 👾 opponent: {count2}')
            else:
                print(f'😎 you: {count}, 👾 opponent: {count2} WINNER 🏆')
            break

    elif coin != chute:
        print(f'💥 {coin}')
        print('❌ errou')
        count2 += 1
        print(f'😎 you: {count}, 👾 opponent: {count2}')
        again = input('🔄 quer ir dnv?(s/n): ')
        if again == 's':
            coin = random.choice(lista)
            continue
        else:
            print('👍 ta bom tchau')
            if count > count2:
                print(f'😎 you: {count} WINNER 🏆, 👾 opponent: {count2}')
            else:
                print(f'😎 you: {count}, 👾 opponent: {count2} WINNER 🏆')

    else:
        print('🤣 é uma moeda man ksks, mas vai dnv 🤭')
        coin = random.choice(lista)
        continue