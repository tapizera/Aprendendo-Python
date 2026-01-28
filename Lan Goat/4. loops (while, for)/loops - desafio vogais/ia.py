word = input("Digite uma palavra: ")
contador = sum(1 for letra in word if letra in 'aeiouAEIOU')
print(f"{word} tem {contador} vogais")