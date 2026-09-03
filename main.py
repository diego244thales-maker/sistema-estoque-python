produtos = []

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

produtos.append(produto)

print("\nProduto cadastrado!")
print(produtos)
