lista_documento = []

lista_autores = []

lista_doc_emprestado = []

lista_usuarios = []

def cadastrar_documento(estado, titulo, data_producao, tema, contexto_hist, desc, autor, loc):
    documentos = {
        'estado': estado,
        'titulo': titulo,
        'data_producao': data_producao,
        'tema': tema,
        'contexto_hist': contexto_hist,
        'desc': desc,
        'autor': autor,
        'loc': loc,
    }

    lista_documento.append(documentos)
    print('\nDocumento cadastrado com Sucesso!!')

def cadastrar_perfil(nome, email, senha):
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
    }
    lista_usuarios.append(usuario)
    print('\nPerfil de usuário cadastrado com Sucesso!!')


def login(email, senha):
    try: 
        for perfil in lista_usuarios:
            if perfil['email'] == email and perfil['senha'] == senha:
                print("Acesso liberado")
            elif perfil['email'] != email or perfil['senha'] != senha:
                raise ValueError("Acesso negado")
            if perfil['email'] != email and perfil['senha'] != senha:
                raise ValueError("Acesso negado")
    except ValueError as Ve:
        print(Ve)
def acessar_documentos():
    for documento in lista_documento:
        print(f"\nNo momento o documento está: {documento['estado']}") 
        print(f"Título: {documento['titulo']}") 
        print(f"Data de produção: {documento['data_producao']}")
        print(f"Tema: {documento['tema']}")
        print(f"Contexto histórico: {documento['contexto_hist']}")
        print(f"Descrição: {documento['desc']}")
        print(f"Autor: {documento['autor']}")
        print(f"Localização na biblioteca: {documento['loc']}")
    

def cadastrar_perfil_autor(nome, data, local_nasc, bio, area_pesquisa):
    autor = {
        'nome': nome, 
        'data': data,
        'local_nasc': local_nasc,
        'bio': bio,
        'area_pesquisa': area_pesquisa,  
    }

    lista_autores.append(autor)
    print('\nPerfil de autor cadastrado com Sucesso!!')

def emprestar_doc(estado, periodo, nome_do_evento, responsavel, tema):
    emprestimo = {
        'estado': estado,
        'periodo': periodo,
        'nome_do_evento': nome_do_evento,
        'responsavel': responsavel,
        'tema': tema, 
    }
    lista_doc_emprestado.append(emprestimo)

    for documento in lista_documento:
        if documento['tema'] == tema:
            print(f"\nEstado do documento: {documento['estado']}")
            print(f"Título: {documento['titulo']}") 
            print(f"Data de produção: {documento['data_producao']}")
            print(f"Tema: {documento['tema']}")
            print(f"Contexto histórico: {documento['contexto_hist']}")
            print(f"Descrição: {documento['desc']}")
            print(f"Autor: {documento['autor']}")
            print(f"Localização na biblioteca: {documento['loc']}")
        
def salvar_infor_documentos():
    with open('documento.txt', 'w') as arquivo:
        for documento in lista_documento:
            linha = (f"\nNo momento o documento está: {documento['estado']}, Título: {documento['titulo']}, Data de produção: {documento['data_producao']}, Tema: {documento['tema']}, Contexto histórico: {documento['contexto_hist']}, Descrição: {documento['desc']}, Autor: {documento['autor']}, Localização na biblioteca: {documento['loc']}") 
            arquivo.write(linha)
            print("Salvo com sucesso")

def salvar_infor_usuario():
    with open('usuario.txt', 'w') as arquivo:
        for usuario in lista_usuarios:
            linha = (f"\nNome: {usuario['nome']}, Email: {usuario['email']}, Senha: {usuario['senha']}")
            arquivo.write(linha)
            print("Salvo com sucesso")

def carregar_arquivo_usuario():
    try: 
        with open('usuario.txt', 'r') as arquivo:
            dados_usuarios = arquivo.read()
            print(dados_usuarios)
    except FileNotFoundError:
        print("Arquivo não encontrado")

def carregar_arquivo_doc():
    try:
        with open('dados.txt', 'r') as arquivo:
            dados_doc = arquivo.read()
            print(f"{dados_doc}")
    except FileNotFoundError:
        print("Arquivo não encontrado")

def ordenar_documento():
    print("Os documentos serão ordenados pelo nome do autor")
    ord = 'autor'
    print("---------------------------------")
    print("1- Ordenar de forma crescente")
    print("2 - Ordenar de forma decrescente")
    print("---------------------------------")

    opc2 = input("Informe uma opção: ")
    if opc2 == '1':
        reverso = False
    elif opc2 == '2':
        reverso = True
    
    for documento in lista_documento:
        ordenar = sorted(lista_documento, key=lambda documento: documento[ord], reverse=reverso)
    
    for documento in ordenar:
        print(f"\nEstado do documento: {documento['estado']}")
        print(f"Título: {documento['titulo']}") 
        print(f"Data de produção: {documento['data_producao']}")
        print(f"Tema: {documento['tema']}")
        print(f"Contexto histórico: {documento['contexto_hist']}")
        print(f"Descrição: {documento['desc']}")
        print(f"Autor: {documento['autor']}")
        print(f"Localização na biblioteca: {documento['loc']}")

def menu():
    while True:
        print("-----------------------------------------------------")
        print("1 - Cadastrar perfil de Autor Obs: essa opção e destinada a autores dos documento")
        print("2 - Cadastrar perfil de usuário")
        print("3 - Cadastrar o documento")
        print("4 - Realizar login")
        print("5 - Acessar documentos históricos")
        print("6 - Pegar emprestado um documento")
        print("7 - Salvar os dados dos documento")
        print("8 - Salvar os dados de usuário")
        print("9 - Ordenar documentos")
        print("10 - Carregar os dados do usuário")
        print("11 - Carregar dados do documento")
        print("12 - Sair")
        print("-----------------------------------------------------")

        opc = input("Informe uma opção: ")

        if opc == '1':
            nome = input("\nNome: ")
            data_nasc = input("Data de nascimento: ")
            local_nasc = input("Local de nascimento: ")
            bio = input("Biografia: ")
            area_pesquisa = input("Área de pesquisa: ")
            cadastrar_perfil_autor(nome, data_nasc, local_nasc, bio, area_pesquisa)    
        elif opc == '2':
            try:
                nome = input("Nome completo: ")
                email = input("Email: ")
                senha = int(input("Senha númerica: "))
                cadastrar_perfil(nome, email, senha)
            except ValueError:
                print("Erro - Informe uma senha válida")
        elif opc == '3':
            estado = 'Livre'
            titulo = input("Titulo do documento: ")
            data_producao = input("Data de produção: ")
            tema = input("Tema: ")
            contexto_hist = input("Contexto histórico: ")
            desc = input("Descrição: ")
            autor = input("Autor: ")
            loc = input("Localização: ")
            cadastrar_documento(estado, titulo, data_producao, tema, contexto_hist, desc, autor, loc)

        elif opc == '4':
            email = input("Email: ")
            senha = input("Senha: ")
            login(email, senha)
        elif opc == '5': 
            acessar_documentos()

        elif opc == '6':
            desejo = input("Deseja pegar um livro emprestado? (S/N): ").upper()
            if desejo == 'S':
                periodo = input("Período: ")
                nome_do_evento = input("Nome do evento: ")
                responsavel = input("Responsável: ")
                tema = input("Tema: ")
                estado = 'Livre'
                emprestar_doc(estado, periodo, nome_do_evento, responsavel, tema)
        elif opc == '7':
            salvar_infor_documentos()
        elif opc == '8': 
            salvar_infor_usuario()
        elif opc == '9':
            ordenar_documento()
        elif opc == '10':
            carregar_arquivo_usuario()
        elif opc == '11':
            carregar_arquivo_doc()
        elif opc == '12':
            print("Encerrando .....")
            break

menu()
