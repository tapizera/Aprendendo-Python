while True:
    resposta = input("Digite uma palavra: ")
    print(f"Palavra digitada: {resposta}")

    vogais = "aeiouAEIOU"
    quantidade = 0

    for v in resposta:
        if v in vogais:
             quantidade += 1

        print(f"Número de vogais: {quantidade}")