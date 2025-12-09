lista = []

def adicionar_livro(titulo, autor,  ano, paginas):
    dic = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'paginas': paginas,
    }
    lista.append(dic)
    print("\nLivro adicionado com sucesso!")

def listar_livros():
    for livro in lista:
        print(f"\nTítulo do livro: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de publicação: {livro['ano']}")
        print(f"Número de páginas: {livro['paginas']}")

def ordenar_livros():
    print('----------------------------------------')
    print("1 - Ordenar pela quantidade de paginas")
    print("2 - Ordenar pelo ano de publicação")
    print('----------------------------------------')

    opc = input("Digite uma opção: ") 

    print('------------------')
    print("1 - Crescente")
    print("2 - Decrescente")
    print('------------------')  

    opc2 = input("Digite uma opção: ") 

    if opc == '1':
        ord = 'paginas'
    elif opc == '2':
        ord = 'ano'

    if opc2 == '1':
        reverso = False
    elif opc2 == '2':
        reverso = True
    
    for livro in lista:
        ordenar = sorted(lista, key=lambda livro: livro[ord], reverse=reverso)

    for livro in ordenar:
        print(f"\nTítulo do livro: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de publicação: {livro['ano']}")
        print(f"Número de páginas: {livro['paginas']}")

def salvar_livros():
    with open('biblioteca.txt', 'w') as arquivo:
        for livro in lista:
            linha = (f"\nTítulo do livro: {livro['titulo']}, Autor: {livro['autor']}, Ano de publicação: {livro['ano']}, Número de páginas: {livro['paginas']}")
            arquivo.write(linha)
        print("Os dados foram salvos no arquivo 'biblioteca.txt'.")

def carregar_livros():
    with open('biblioteca.txt', 'r') as arquivo:
            livros = arquivo.read()
            print(livros)

def menu():
    while True:
        print('--------------------------')
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Ordenar livros")
        print("4 - Salvar livros")
        print("5 - Carregar livros")
        print('--------------------------')
        opc = input("Digite uma opção: ")
        if opc == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            ano = int(input("Ano de publicação: "))
            paginas = int(input("Quantidade de paginas: "))
            adicionar_livro(titulo, autor, ano, paginas)
        elif opc == '2':
            listar_livros()
        elif opc == '3':
            ordenar_livros()
        elif opc == '4':
            salvar_livros()
        elif opc == '5':
            carregar_livros()
menu()