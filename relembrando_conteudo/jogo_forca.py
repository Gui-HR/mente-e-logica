#Jogo da forca, usando loops.

secret_word = 'abobora'
lifes = 5
user_word = []
letters_tried = []

for letter in secret_word:
    user_word.append('_' )

print(f'Vamos jogar forca, tente adivinhar qual é a palavra. A palavra tem {len(secret_word)} letras.')

while lifes > 0:
    str_user_word = ' '.join(user_word)
    str_letters_tried = '-'.join(letters_tried)

    print(f'\n---------------------------------------------------------\n\nA palavra é {str_user_word}. \nVoce tem {lifes} vidas para tentar.\nVocê já tentou as letras {str_letters_tried}.\n\n---------------------------------------------------------\n')

    user_letter = input(f'Digite uma letra pra tentar advinhar a palavra: ').lower()

    print(f'\n---------------------------------------------------------\n')


    if user_letter in letters_tried:
         print('Você já tentou esta letra, tente outra.')
         continue

    letters_tried.append(user_letter)

    if not user_letter in secret_word:
        print(f'Errou, a palavra não tem a letra {user_letter}.')

        lifes -= 1

        continue

    print(f'Acertou, a palavra tem a letra {user_letter}.')

    for i in range(len(secret_word)):
            if secret_word[i] == user_letter:
                user_word.pop(i)
                user_word.insert(i, user_letter)

    if ''.join(user_word) == secret_word:
        print(f'\n---------------------------------------------------------\nParabens, você advinhou a palavra secreta! {secret_word}')

        break