import random

class Difficult:
    def __init__(self, name, call, lifes, multiplier):
        self.name = name
        self.call = call
        self.lifes = lifes
        self.multiplier = multiplier

difficult_levels = [Difficult('Facil', 'f', 10, 5),
                    Difficult('Medio', 'm', 7, 15),
                    Difficult('Dificil', 'd', 5, 35)]
story_score = []

def print_error(error): print(f'\n{error} não é um valor valido, tente novamente\n\n----------------------------------------------\n')

def treat_lists(list,reverse):
    number = str(attempt_number) if list == tries else attempt_number 

    list.append(number)
    list.sort(reverse=reverse)

def choose_difficult(): 
    while True:
        print('Escolher a dificuldade do jogo, esta vai definir quantas tentativas você tem para adivinhar o número\n')
        
        for difficult in difficult_levels:
            if len(difficult.name) == 5: spaces = '   '
            else: spaces = ' ' 

            print(f'{difficult.name}{spaces}| {difficult.lifes}')

        selected_difficult = input('\nDigite: "f" para FACIL /-/ "m" para MÉDIO /-/ "d" para DIFICIL: ')

        if not selected_difficult in ['f', 'm', 'd']:
            print_error(selected_difficult)
            continue

        for difficult in difficult_levels:
            if selected_difficult == difficult.call:
                lifes = difficult.lifes
                multiplier = difficult.multiplier
                break

        return lifes, multiplier

def input_validation():
    while True:
        validate_number = input('Digite um número entre 0 - 100: ')

        if not validate_number.isdigit():
            print_error(validate_number)
            continue

        if not validate_number in tries: return int(validate_number)

        print('\nVocê já tentou esse número, tente outro!\n\n----------------------------------------------\n')
        continue

def show_score():
    score = multiplier * (lifes - len(tries))
    story_score.append(str(score))

    print(f'\nSua pontuação foi de {score} pontos\n\nSua pontuação anterior: {'pts - '.join(story_score)}pts')

print('----------------------------------------------\n\n ADIVINHE O NÚMERO\n\n----------------------------------------------\n')

while True:
    play = input('Para JOGAR digite "j" /-/ Para SAIR digite "s": ').lower()

    if play == 's':
        print('\nSaindo...')
        break

    if play != 'j':
         print_error(play)
         continue
    
    print('\nVamos jogar!\n\n----------------------------------------------\n')
    
    lifes, multiplier = choose_difficult() 

    print('\n----------------------------------------------\n')

    secret_number = random.randint(0,100)
    higher = [100]
    lesser = [0]
    tries = []

    while True:
        attempt_number = input_validation()

        if attempt_number > secret_number:
            print(f'\n{attempt_number} é maior que o número secreto.')
            treat_lists(higher,False)

        if attempt_number < secret_number:
            print(f'\n{attempt_number} é menor que o número secreto.')
            treat_lists(lesser, True)

        if attempt_number == secret_number: 
            print(f'\nParabéns você acertou, o número secreto é {secret_number}')
            show_score()
            break

        print('\n----------------------------------------------\n')

        treat_lists(tries, False)

        if lifes - len(tries) == 0:
            print(f'Você perdeu, suas vidas acabaram. O número secreto era {secret_number}')
            show_score()
            break

        print(f'Você ainda tem {lifes - len(tries)} vidas.')
        print(f'\nO número secreto esta entre: {lesser[0]} < ?? > {higher[0]}')
        print(f'\nNúmeros já tentados: {' - '.join(tries)}\n\n----------------------------------------------\n')
    
    print('\n----------------------------------------------\n\nDeseja jogar novamente?\n')
    
#TAREFAS

# FEITO
#   - Arrumar um jeito para mostrar os números, "O número secreto esta entre: 0 < ?? > 100".
#       ° Ver direito a ordem das listas.
#   - Espaçamento do texto.
#   - Arrumar erro do loop quando termina o jogo.
#   - Mostrar os números ja tentados
#   - Sistema para escolher a dificuldade.
#       ° usar um for para ver todas as possibilidades
#   Refatorar o código