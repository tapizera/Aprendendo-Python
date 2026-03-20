inteiro = input("bota um numero int: ")
flutuante = input("agr um numero float: ")
booleano = input("e por fim um bool: ")

inteiro = int(inteiro)
flutuante = float(flutuante)
booleano = bool(booleano)

print("Valores convertidos:")

print(f"- Número inteiro: {inteiro} (tipo: {type(inteiro)}")

print(f"- Número flutuante: {flutuante} (tipo {type(flutuante)})")

print(f"- Valor booleano: {booleano} (tipo: {type(booleano)})")