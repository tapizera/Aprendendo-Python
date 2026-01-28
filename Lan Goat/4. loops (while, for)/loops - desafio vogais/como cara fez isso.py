word = input("Digite uma palavra: ")
chars = []
for char in range(len(word)):
    if word[char] == "a" or word[char] == "e" or word[char] == "i" or word[char] == "o" or word[char] == "u":
        chars.append(word[char])
print(f"A palavra '{word}' tem {len(chars)} vogais")