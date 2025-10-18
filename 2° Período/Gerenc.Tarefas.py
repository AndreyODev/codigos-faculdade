tarefas = []
def adicionar_tarefa(lista_tarefas, id, descricao, status, prioridade):
    tarefa = { 
        "id": id, 
        "descricao": descricao, 
        "status": status, 
        "prioridade": prioridade
        }
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada")

def visualizar_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        print(f"ID: {tarefa["id"]} | Descrição: {tarefa["descricao"]} | Status: {tarefa["status"]} | Prioridade: {tarefa["prioridade"]}")
    print("\n")
def filtrar_tarefas(lista_tarefas, status = None, prioridade = None):
    tarefas_filtradas = []
    for tarefa in lista_tarefas:
        if tarefa['status'] == status and tarefa['prioridade'] == prioridade:
            tarefas_filtradas.append(tarefa)
            visualizar_tarefas(tarefas_filtradas)
        elif tarefa['status'] == status or tarefa['prioridade'] == prioridade:
            tarefas_filtradas.append(tarefa)
            visualizar_tarefas(tarefas_filtradas)
        elif status is None and prioridade is None:
            tarefas_filtradas = lista_tarefas
            visualizar_tarefas(tarefas_filtradas)
            break
        elif status is None or prioridade is None:
            tarefas_filtradas = lista_tarefas
            visualizar_tarefas(tarefas_filtradas)
            break
def menu():
    id = 1
    while True:
        print("------------------------------------")
        print("Digite 1 para adicionar as tarefas")
        print("Digite 2 para visualizar as tarefas")
        print("Digite 3 para filtrar as tarefas")
        print("Digite 4 para sair")
        print("------------------------------------")
        opc = input("Informe um número: ")
        if opc == "1":
            print(f"Identificador: {id}")
            descricao = input("Informe uma descrição para a tarefa: ")
            status = input("Qual o status da tarefa. Pendente, em andamento, concluída? ").lower()
            prioridade = input("Qual o grau da tarefa. Alta, média, baixa? ").lower()
            adicionar_tarefa(tarefas, id, descricao, status, prioridade)
            id += 1
        elif opc == "2":
            visualizar_tarefas(tarefas)
        elif opc == "3":
            print("-------------------------------------------------------")
            print("Digite 1 filtrar a tarefa pelo status")
            print("Digite 2 filtrar a tarefa pela prioridade")
            print("Digite 3 filtrar a tarefa pelo status e pela prioriade")
            print("-------------------------------------------------------")
            N = input("Informe um número: ")
            if N == "1":
                status = input("Informe o status para filtrar as tarefas(Pendente, em andamento, concluida): ").lower()
                filtrar_tarefas(tarefas, status=status)
            if N == "2":
                prioridade = input("Informe a prioridade para filtrar as tarefas(Alta, Media, Baixa): ").lower()
                filtrar_tarefas(tarefas, prioridade=prioridade)
            if N == "3":
                status = input("Informe o status para filtrar as tarefas(Pendente, em andamento, concluida): ").lower()
                prioridade = input("Informe a prioridade para filtrar as tarefas(Alta, Media, Baixa): ").lower()
                filtrar_tarefas(tarefas, status=status, prioridade=prioridade)
        elif opc == "4":
            print("Saindo......")
            break
                 
menu()