# variáveis
hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00


# input (entrada de dados)
print(f"--- Bem vindo ---")
print(f"- hamburguer ----- 10.50")
print(f"- batata frita --- 4.00")
print(f"- refrigerante --- 3.00")

quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))

quantidade_batata = int(input("Digite a quantidade de batatas fritas desejadas: "))

quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))


# cálculo do preço total
preco_total = (hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante)

# output (saída de dados)
print("O preço total do seu pedido é: R$", preco_total)