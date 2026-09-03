produtos = []

while True:
    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        print("\n=== PRODUTOS CADASTRADOS ===")

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(
                    f"Produto: {produto['nome']} | "
                    f"Preço: R$ {produto['preco']:.2f} | "
                    f"Quantidade: {produto['quantidade']}"
                )

    elif opcao == "3":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")
