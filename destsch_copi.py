def unidade(n):
    unidades = ["", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
    return unidades[n]

def dezena(n):
    dezenas = ["", "zehn", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
    return dezenas[n]

def numero_ate_99(n):
    if n < 10:
        return unidade(n)
    elif 10 <= n <= 12:
        especiais = {10: "zehn", 11: "elf", 12: "zwölf"}
        return especiais[n]
    elif 13 <= n <= 19:
        bases = {13: "dreizehn", 14: "vierzehn", 15: "fünfzehn", 16: "sechzehn", 17: "siebzehn", 18: "achtzehn", 19: "neunzehn"}
        return bases[n]
    else:
        u = n % 10
        d = n // 10
        if u == 0:
            return dezena(d)
        else:
            return unidade(u) + "und" + dezena(d)

def numero_em_alemao(n):
    if n < 100:
        return numero_ate_99(n)
    elif n < 1000:
        c = n // 100
        resto = n % 100
        prefixo = "einhundert" if c == 1 else unidade(c) + "hundert"
        return prefixo + (numero_ate_99(resto) if resto else "")
    elif n < 1000000:
        milhar = n // 1000
        resto = n % 1000
        prefixo = "eintausend" if milhar == 1 else numero_ate_99(milhar) + "tausend"
        return prefixo + (numero_em_alemao(resto) if resto else "")
    elif n == 1000000:
        return "eine Million"
    else:
        return "Número muito grande pra esse tradutor 😅"

# Funcionamento
while True:
    try:
        n = int(input("Digite um número: "))
        print(f"{n} em alemão é: {numero_em_alemao(n)}")
    except ValueError:
        print("Por favor, digite um número válido.")
