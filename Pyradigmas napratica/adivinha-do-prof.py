from random import randint

print("=" * 50)
print("🎯 BEM-VINDO AO JOGO DE ADIVINHAÇÃO EM PYTHON 🎯")
print("=" * 50)

# Escolha do nível
print("\nEscolha o nível de dificuldade:")
print("1 - Fácil (número entre 1 e 10)")
print("2 - Médio (número entre 1 e 50)")
print("3 - Difícil (número entre 1 e 100)")

nivel = input("Digite o nível desejado (1, 2 ou 3): ")

if nivel == "1":
    limite = 10
    tentativas = 5
elif nivel == "2":
    limite = 50
    tentativas = 7
elif nivel == "3":
    limite = 100
    tentativas = 10

else:
    print("\nOpção inválida. O jogo será iniciado no modo Fácil.")
    limite = 10
    tentativas = 5

numero_secreto = randint(1, limite)
pontos = 100

print(f"\n✅ O computador escolheu um número entre 1 e {limite}.")
print(f"Você tem {tentativas} tentativas para acertar!\n")

for rodada in range(1, tentativas + 1):
    print(f"--- Tentativa {rodada} de {tentativas} ---")

    palpite_texto = input("Digite seu palpite: ")

    # Verificação para evitar erro caso o usuário digite texto
    if not palpite_texto.isdigit():
        print("⚠️ Você deve digitar apenas números inteiros.\n")
        continue

    palpite = int(palpite_texto)

    if palpite < 1 or palpite > limite:
        print(f"⚠️ Digite um número entre 1 e {limite}.\n")
        continue

    if palpite == numero_secreto:
        print(f"\n🎉 Parabéns! Você acertou o número secreto: {numero_secreto}")
        print(f"🏆 Sua pontuação final foi: {pontos} pontos")
        break
    else:
        diferenca = abs(numero_secreto - palpite)
        pontos -= diferenca

        if palpite < numero_secreto:
            print("📉 O número secreto é MAIOR que o seu palpite.")
        else:
            print("📈 O número secreto é MENOR que o seu palpite.")

        # Dica extra
        if diferenca <= 3:
            print("🔥 Você está muito perto!")
        elif diferenca <= 10:
            print("🙂 Está chegando...")
        else:
            print("❄️ Ainda está longe...")

        print(f"⭐ Pontuação atual: {pontos}\n")

else:
    print("\n😢 Suas tentativas acabaram!")
    print(f"O número secreto era: {numero_secreto}")
    print(f"Sua pontuação final foi: {pontos}")
    
print("\nObrigado por jogar!")
print("=" * 50)