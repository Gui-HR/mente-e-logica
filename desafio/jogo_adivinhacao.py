import random

lives = 7
score = []
difficulty = '0'
guesses = []

while True:
    print('\n=========== Adivinhe o Número ===========')

    if score == []:    
        print('\nBem vindo(a) ao jogo Advinhe o Número!')
        print(f'\nNeste jogo você terá algumas vidas, para acertar. A cada tentativa uma vida é perdida')
        print('Quanto menos vidas você gastar para advinhar o número, mais pontos você fará')
        print('\n-----------------------------------------')

    while True:
        play_game = input('\nDigite "j" para jogar ou "s" para sair: ').lower()

        try:
            if play_game != 'j' and play_game != 's':
                raise TypeError()
        except:
            print('\nInsira um valor valido (j/s).')
        else:
            break
    
    print('\n-----------------------------------------\n')
    
    if play_game == 's':
        print('Desconectando...\n')
        break

    while difficulty != '1' and difficulty != '2' and difficulty != '3':
        print('Escolha a dificuldade do jogo, quanto mais dificil mais pontos serão feitos.\n')
        print('Facil   | 10 tentativas.')
        print('Normal  | 07 tentativas.')
        print('Difícil | 05 tentativas.')
        print('\nDigite 1 para facil, 2 para normal e 3 para dificil"\n')

        difficulty = input('Em qual dificuldade você deseja jogar: ')

        if difficulty == '1':
             lives = 10
             score_multiplier = 5
             break
        elif difficulty == '2':
            lives = 7
            score_multiplier = 15
            break
        elif difficulty == '3':
            lives = 5
            score_multiplier = 35
            break

        print('\n-------------------XXX-------------------\n')
        print('Digite um valor valido para selecionar a dificuldade!\n')
        continue

    print('\n-----------------------------------------\n')
    print('Vamos jogar!\n')

    secret_number = random.randint(0, 100)

    while play_game == 'j':
        print('-----------------------------------------')

        if guesses != []: 
            print(f'\nPalpites já feitos: {' - '.join(guesses)}')
            
        user_input = input('\nDigite um número inteiro entre 0 e 100: ')

        if not user_input.isdigit():
            print('\n-------------------XXX-------------------')
            print('\nO valor inserido precisa ser um número inteiro entre 0 e 100. Tente novamente...\n')
            continue
        else:
            attempt = int(user_input)
            if attempt > 100 or attempt < 0:
                print('\n-------------------XXX-------------------')
                print('\nO valor inserido precisa ser um número inteiro entre 0 e 100. Tente novamente...\n')
                continue

            if str(attempt) in guesses:
                print('\n-------------------XXX-------------------')
                print('\nVocê já tentou esse número, tente outro...\n')
                continue

        print('\n-------------------///-------------------')

        if attempt != secret_number:
            print('\nVocê errou! Faça outra tentativa.\n')

            if attempt < secret_number:
                print(f'Dica: O número é maior do que {attempt}.\n')
            else:
                print(f'Dica: O número é menor do que {attempt}.\n')
            
            lives -= 1

            if lives != 0:
                print(f'Você tem {lives} vidas sobrando!\n')

        else:
            score.append(str(lives * score_multiplier))

            print(f'\nParabéns você acertou, o número é {secret_number}!')
            print(f'\nVocê ainda tinha {lives} vidas sobrando!')
            print(f'\nSua pontuação foi de {lives * score_multiplier} pts')

        if lives == 0:
            score.append('0')

            print(f'Você perdeu! Suas vidas acabaram, o número era {secret_number}.')
            print('Você não fez pontos nessa partida.')

        guesses.append(str(attempt))

        if lives == 0 or attempt == secret_number:
            lives = 7
            difficulty = '0'
            
            print('\n-----------------------------------------')
            print(f'\nSuas pontuações são: {' pts | '.join(score)} pts\n')
            break

