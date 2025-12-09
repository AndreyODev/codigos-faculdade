lista = []

def adicionar_produto(nome, categoria, preco, quantidade):
    dic = {
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'quantidade': quantidade,
    }
    lista.append(dic)

    print("\nProduto adicionado com sucesso!")

def atualizar_quantidade(nome):
    for produto in lista:
        if produto['nome'] == nome:
            qtd = input("Informe a nova quantidade: ")
            produto['quantidade'] = qtd
            print(f"\nNome do produto: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Preço: {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")

def listar_produtos():
    for produto in lista:
        print(f"\nNome do produto: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")

def salvar_estoque():
    with open('estoque.txt', 'w') as arquivo:
        for produto in lista:
            linha = (f"\nNome do produto: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            arquivo.write(linha)

def carregar_estoque():
    with open('estoque.txt', 'r') as arquivo:
        arquivo.read()

def menu():
    while True:
        print('----------------------------------------')
        print("1 - Adicionar produto")
        print("2 - Atualizar a quantidade de produto")
        print("3 - listar produtos")
        print("5 - Salvar dados em arquivo")
        print('----------------------------------------')
        opc = input("Informe uma opção: ")

        if opc == '1':
            nome = input("\nNome do produto: ").lower()
            categoria = input("Categoria: ").lower()
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, categoria, preco, quantidade)
        elif opc == '2':
            listar_produtos()
            nome = input("Informe o nome do produto: ")
            atualizar_quantidade(nome)
        elif opc == '3':
            listar_produtos()
        elif opc == '5':
            salvar_estoque()
menu()