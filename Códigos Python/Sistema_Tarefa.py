import random

tarefas = []

def adicionar_tarefa(id, lista_tarefas, descricao, status, prioridade):
    tarefa = {"id": id, "descricao": descricao, "status": status, "prioridade": prioridade}
    lista_tarefas.append(tarefa)

def visualizar_tarefas(lista_tarefas):
    if lista_tarefas:
        for tarefa in lista_tarefas:
            print(tarefa)
    else:
        print("Nenhuma tarefa disponível.")

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    # Implementar lógica de filtro
    pass

def menu():
    while True:
        print("------------------------------------")
        print("Digite 1 para adicionar as tarefas")
        print("Digite 2 para visualizar as tarefas")
        print("Digite 3 para filtrar as tarefas")
        print("Digite 4 para sair")
        opc = input("Informe um número: ")

        if opc == "1":
            id = random.randint(1, 100)
            print(f"Identificador: {id}")
            descricao = input("Informe uma descrição para a tarefa: ")
            status = input("Qual o status da tarefa. Pendente, em andamento, concluída? ").lower()
            prioridade = input("Qual o grau da tarefa. Alta, média, baixa? ").lower()

            adicionar_tarefa(id, tarefas, descricao, status, prioridade)

        elif opc == "2":
            visualizar_tarefas(tarefas)

        elif opc == "3":
            # Implementar a lógica de filtragem aqui
            pass

        elif opc == "4":
            print("Saindo do programa...")
            break  # Quebra o loop e sai do programa

        else:
            print("Opção inválida, tente novamente.")

# Exemplo de como executar o menu
menu()