#lista de tarefas
task_list = []
options = ['Listar Tarefas', 'Adicionar Tarefa', 'Remover Tarefa', 'Sair']

def print_list(list):
    for index in range(len(list)):
                if index == 0: print()

                print(f'{index +  1} - {list[index]}')

def validation_loop(list, action, selection): 
     while True:
        user_try = input(f'\nDigite o número correspondente a {selection} que deseja {action}: ')

        if user_try.isdigit():
            user_action = int(user_try)
        
            if user_action >= 1 and user_action <= len(list): return user_action
            
        print(f'\nEssa {selection} é invalida, tente novamente!\n\n---------------------------------------------------------\n')
        continue

print('\n---------------------------------------------------------\n\nLISTA DE TAREFAS')

while True:
    print('\n---------------------------------------------------------\nOPÇÕES')

    print_list(options)

    print('\n---------------------------------------------------------\nENTRADA')

    user_action = validation_loop(options, 'selecionar', 'opção')

    if user_action == 1:
        print('\nVocê não tem tarefas disponiveis no momento, crie uma para vizualiza-lá.') if len(task_list) == 0 else print_list(task_list)
        continue

    if user_action == 2:
        new_task = input('\nDigite qual será a nova tarefa adicionada: ')
        task_list.append(new_task)

        print(f'\nA tarefa {new_task} foi adicionada!')
        continue

    if user_action == 3:
        if len(task_list) == 0:
            print('\nVocê não tem tarefas no momento!')
            continue

        print_list(task_list)

        removed_task = validation_loop(task_list, 'remover', 'tarefa')
        
        print(f'\nA tarefa {task_list[removed_task - 1]} foi removida!')

        task_list.pop(removed_task - 1)
        continue

    if user_action == 4:
       print('\nSaindo...\n')
       break