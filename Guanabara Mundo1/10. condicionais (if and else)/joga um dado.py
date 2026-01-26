import random
count = 0     
count2 = 0
dado = random.randint (1,6)
while True:
    chute = int(input('🎲 chuta um número de 1 a 6: '))
    if chute == dado:
        print(f'💥 {dado}')
        print('✔️  acertou')
        count += 1
        print(f'😎 you: {count}, 👾 opponent: {count2}')
        again = input('🔄 quer ir dnv?(s/n): ')
        if again == 's':
            dado = random.randint (1,6)
            continue
        else:
            print('👍 ta bom tchau')
            if count > count2:
                print(f'😎 you: {count} WINNER 🏆, 👾 opponent: {count2}')
            else:
                print(f'😎 you: {count}, 👾 opponent: {count2} WINNER 🏆')
            break

    elif chute < 1 or chute > 6:
        print('🤣 é um dado man ksks, mas vai dnv 🤭')
        dado = random.randint (1,6)
        continue

    else:
        print(f'💥 {dado}')
        print('❌ errou')
        count2 += 1
        print(f'😎 you: {count}, 👾 opponent: {count2}')
        again = input('🔄 quer ir dnv?(s/n): ')
        if again == 's':
            dado = random.randint (1,6)
            continue
        else:
            print('👍 ta bom tchau')
            if count > count2:
                print(f'😎 you: {count} WINNER 🏆, 👾 opponent: {count2}')
            else:
                print(f'😎 you: {count}, 👾 opponent: {count2} WINNER 🏆')