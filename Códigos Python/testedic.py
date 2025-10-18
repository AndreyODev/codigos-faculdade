lista_tarefas = []
def adicionar_tarefa(lista_tarefas, id, descricao, status, prioridade):
    tarefa = {
        "id": id,
        "descrição": descricao,
        "status": status,
        "prioridade": prioridade
    }

    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso")
def visualizar_tarefas(lista_tarefas):
    print(lista_tarefas)
def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = []
    for tarefa in lista_tarefas :
        if  status is None or tarefa["status"] == status and prioridade is None or tarefa["prioridade"]: 
            tarefas_filtradas.append(tarefa)
            visualizar_tarefas(tarefas_filtradas)

def menu():
    while True:
        print("------------------------")
        print("Digite 1 para add")
        print("Digite 2 para visualizar")
        print("Digite 3 para filtrar")
        print("Digite 4 para sair")
        print("------------------------")
        opc = input("Informe um número: ")
        if opc == "1":
            if lista_tarefas: 
                id = max(tarefa["id"] for tarefa in lista_tarefas) +1
            else: 
                id = 1
            print(f"Identificador: {id}")
            descricao = input("Informe uma descrição para a tarefa: ")
            status = input("Qual o status da tarefa [Pendente, Em andamento, Concluída]? ")
            prioridade = input("Qual o nível de prioridade [Alta, Média, Baixa]?  ")    
            adicionar_tarefa(lista_tarefas, id, descricao, status, prioridade)
        elif opc == "2":
            visualizar_tarefas(lista_tarefas)
        elif opc == "3":
            print("------------------------")
            print("Digite 1 para filtrar pelo status: ")
            print("Digite 2 para filtrar pela prioriade: ")
            print("Digite 3 para filtrar pelo status e prioriade: ")
            print("------------------------")
            n = input("Informe um número: ")
            if n == "1":
                status = input("Informe o status: ")
                filtrar_tarefas(lista_tarefas, status=status)
            if n == "2":
                prioridade = input("Informe a prioridade: ")
                filtrar_tarefas(lista_tarefas, prioridade=prioridade)
            if n == "3":
                status = input("Informe o status: ")
                prioridade = input("Informe a prioridade: ")
                filtrar_tarefas(lista_tarefas, status=status, prioridade=prioridade)
        elif opc == "4":
            print("Saindo")
            break

menu()