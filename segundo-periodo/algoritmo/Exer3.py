lista = []

def adicionar_produto(nome, categoria, preco, quantidade):
    dic = {
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'quantidade': quantidade,
    }
    lista.append(dic)
    print(f"\nNome do produto: {dic['nome']}")
    print(f"Categoria: {dic['categoria']}")
    print(f"Preço: {dic['preco']}")
    print(f"Quantidade: {dic['quantidade']}\n")
    print("Produto adicionado com sucesso!")

def atualizar_quantidade(nome):
    for produto in lista:
        if produto['nome'] == nome:
            qtd = int(input("Qual a nova quantidade? "))
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

def ordenar_produtos():
    print("-----------------------------")  
    print("1 - Ordenar pelo preço")
    print("2 - Ordenar pela quantidade")
    print("-----------------------------")  

    opc = input("Digite um número: ")

    print("----------------")  
    print("1 - Crescente")
    print("2 - Descrente")
    print("----------------") 

    ord_produtos = input("Digite um número: ")
        
    if opc == '1':
        ord = 'preco'
    elif opc == '2':
        ord = 'quantidade' 
    
    if ord_produtos == '1': 
        reverso = False
    elif ord_produtos == '2': 
        reverso = True 

    for produto in lista: 
        ordenar = sorted(lista, key=lambda produto: produto[ord], reverse=reverso)

    for produto in ordenar:
        print(f"\nNome do produto: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")
    
def salvar_estoque():
    with open('estoque.txt', 'w') as arquivo:
        for produto in lista:
            linha = (f"\nNome do produto: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            arquivo.write(linha)
        print("Os dados foram salvos no arquivo 'estoque.txt'")

def carregar_estoque():
    with open('estoque.txt', 'r') as arquivo:
        estoque = arquivo.read()
        print(estoque)
        
def menu():
    while True:
        print("-----------------------------")    
        print("1 - Adicionar produto")
        print("2 - Atualizar a quantidade")
        print("3 - Listar produtos")
        print("4 - Ordenar produtos")
        print("5 - Salvar Estoque")
        print("6 - Carregar Estoque")
        print("7 - Sair")
        print("-----------------------------")   
        opc = input("Digite um número: ")
        if opc == '1':
            nome = input("Informe o nome do produto: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            adicionar_produto(nome, categoria, preco, qtd)
        elif opc == '2':
            nome = input("Informe o nome do produto: ")
            atualizar_quantidade(nome)
        elif opc == '3':
            listar_produtos()
        elif opc == "4":
            ordenar_produtos()
        elif opc == '5':
            salvar_estoque()
        elif opc == '6':
            carregar_estoque()

menu()

