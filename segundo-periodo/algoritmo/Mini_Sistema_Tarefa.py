tarefas = []

def adicionar_tarefa(lista_tarefas, id, descricao, status, prioridade):
    tarefa = {
        "id": id, 
        "descricao": descricao, 
        "status": status, 
        "prioridade": prioridade
    }
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada\n")

def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa encontrada.\n")
    else:
        for tarefa in lista_tarefas:
            print(f"ID: {tarefa['id']} | Descrição: {tarefa['descricao']} | Status: {tarefa['status']} | Prioridade: {tarefa['prioridade']}")
        print("\n")

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = []
    
    for tarefa in lista_tarefas:
        if (status is None or tarefa['status'] == status) and (prioridade is None or tarefa['prioridade'] == prioridade):
            tarefas_filtradas.append(tarefa)

    if tarefas_filtradas:
        visualizar_tarefas(tarefas_filtradas)
    else:
        print("Nenhuma tarefa encontrada com esses critérios.\n")

def menu():
    id_contador = 1  # contador para gerar IDs únicos

    while True:
        print("------------------------------------")
        print("Digite 1 para adicionar as tarefas")
        print("Digite 2 para visualizar as tarefas")
        print("Digite 3 para filtrar as tarefas")
        print("Digite 4 para sair")
        print("------------------------------------")
        opc = input("Informe um número: ")

        if opc == "1":
            descricao = input("Informe a descrição da tarefa: ")
            status = input("Qual o status da tarefa (pendente, em andamento, concluída)? ").lower()
            prioridade = input("Qual o grau da tarefa (alta, média, baixa)? ").lower()

            adicionar_tarefa(tarefas, id_contador, descricao, status, prioridade)
            id_contador += 1  # incrementa o ID para a próxima tarefa

        elif opc == "2":
            visualizar_tarefas(tarefas)

        elif opc == "3":
            print("-------------------------------------------------------")
            print("Digite 1 para filtrar pelo status")
            print("Digite 2 para filtrar pela prioridade")
            print("Digite 3 para filtrar pelo status e pela prioridade")
            print("-------------------------------------------------------")
            opc_filtro = input("Informe um número: ")

            if opc_filtro == "1":
                status = input("Informe o status para filtrar as tarefas (pendente, em andamento, concluída): ").lower()
                filtrar_tarefas(tarefas, status=status)

            elif opc_filtro == "2":
                prioridade = input("Informe a prioridade para filtrar as tarefas (alta, média, baixa): ").lower()
                filtrar_tarefas(tarefas, prioridade=prioridade)

            elif opc_filtro == "3":
                status = input("Informe o status para filtrar as tarefas (pendente, em andamento, concluída): ").lower()
                prioridade = input("Informe a prioridade para filtrar as tarefas (alta, média, baixa): ").lower()
                filtrar_tarefas(tarefas, status=status, prioridade=prioridade)

        elif opc == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

menu()