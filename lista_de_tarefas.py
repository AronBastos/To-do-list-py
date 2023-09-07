
lista_de_tarefas = []


def adicionar_tarefa(tarefa):
    lista_de_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada à lista.")


def remover_tarefa(tarefa):
    if tarefa in lista_de_tarefas:
        lista_de_tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida da lista.")
    else:
        print(f"Tarefa '{tarefa}' não encontrada na lista.")


def exibir_tarefas():
    if not lista_de_tarefas:
        print("A lista de tarefas está vazia.")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(lista_de_tarefas, start=1):
            print(f"{i}. {tarefa}")

# Loop principal para interagir com o usuário
while True:
    print("\nOpções:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Exibir Tarefas")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefa)
    elif escolha == "2":
        tarefa = input("Digite a tarefa que deseja remover: ")
        remover_tarefa(tarefa)
    elif escolha == "3":
        exibir_tarefas()
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
