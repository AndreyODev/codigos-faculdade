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

def atualizar_produtos(atualizar):
    for produto in lista:
        if produto['nome'] == atualizar:
            qtd = int(input("Informe a nova quantidade: "))
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

def ordernar_produtos():
    while True:
        try:
            print("------------------------")
            print("1 - Ordenar pela quantidade")
            print("2 - Ordenar pelo preço")
            print("3 - Sair")
            print("------------------------")
            opc = input("Informe uma opção: ")

            if opc == '1':
                ord = 'quantidade'

            elif opc == '2':
                ord = 'preco'
            elif opc == '3':
                break
            else:
                raise ValueError("Erro - Opção inválida")
            
            print("-----------------------------------")
            print("1 - Ordenar de forma crescente")
            print("2 - Ordenar de forma decrescente")
            print("-----------------------------------")

            opc2 = input("Informe uma opção: ")

            if opc2 == '1':
                reverso = False
            elif opc2 == '2':
                reverso = True
            
            else:
                raise ValueError("Erro - Opção inválida")
            
            for produto in lista:
                ordenar = sorted(lista, key=lambda produto: produto[ord], reverse=reverso)
            
            for produto in ordenar:
                print(f"\nNome do produto: {produto['nome']}")
                print(f"Categoria: {produto['categoria']}")
                print(f"Preço: {produto['preco']}")
                print(f"Quantidade: {produto['quantidade']}")
        except ValueError as Ve:
            print(Ve)

def menu():
    while True:
        print("------------------------")
        print("1 - Adicionar produto")
        print("2 - Atualizar a quantidade do produto")
        print("3 - Listar produtos")
        print("4 - Ordenar produtos")
        print("------------------------")
        opc = input("Informe uma opção: ")

        if opc == '1':
            nome = input("Nome do produto: ").lower()
            categoria = input("Categoria: ").lower()
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, categoria, preco, quantidade)
        elif opc == '2':
            listar_produtos()
            atualizar = input("Informe o nome do produto que deseja atualizar: ").lower()
            atualizar_produtos(atualizar)
        elif opc == '3':
            listar_produtos()
        elif opc == '4':
            ordernar_produtos()

menu()