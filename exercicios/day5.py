# Ex 01

# for i in range(1, 11):
#     print(i)

# Ex 02
# N = int(input('Insira um numero para ver sua soma de 1 até esse N°:'))
# sum = 0

# for i in range(1, N + 1):
#         sum += i

# print(sum)

# Ex 03
# number = int(input('Insira o numero que deseja saber a tabuada: '))

# for i in range(1, 11):
#     result = i * number
#     print(f'{i} X {number} = {result}')

# Ex 04
# even_numbers = 0
# odd_numbers = 0

# for i in range(1, 21):
#     if i % 2 == 0:
#         even_numbers += 1
#     else:
#         odd_numbers += 1

# print('Numeros pares', even_numbers)
# print('Numeros impares', odd_numbers)

# Ex 05
# import random

# correct_number = random.randint(1, 100)
# tries = 0
# user_number = 0

# while user_number != correct_number:
#     tries += 1
#     user_number = int(input('Tente advinhar o número: '))

#     if user_number == correct_number:
#         print('Parabens, você acertou o número!!!')
#         print('O número era', correct_number)
#         print(f'Você acertou em sua {tries}° tentativa!')
#         break

#     if user_number < correct_number:
#         print('O número é maior que', user_number)
#     else:
#         print('O número é menor que', user_number)

#     print(f'Essa foi sua {tries}° tentativa!')

# Extra 01
# number = int(input('Digite um número interito positivo para ver seu fatorial: '))

# factorial = 1

# if number < 0:
#     print('Não existe fatorial de número negativo')
# elif number == 0 or number == 1:
#     print(f'O fatorial de {number} é 1')
# else: 
#     for i in range(1, number + 1):
#         factorial *= i

#     print(f'O fatorial de {number} é {factorial}')  

# Extra 02
# fibonacci = 0
# after = 1
# counter = 0

# quantity = int(input('Quantos números da sequencia de Fibonacci você deseja ver?'))

# if quantity == 0:
#     print('Insira um número maior que 0')
# elif quantity == 1:
#     print(f'A sequencia de Fibonacci até {quantity}, é {after}')
# else:
#     print('Serie Fibonacci:')
#     while counter <= quantity:
#         print(fibonacci)
#         aux = fibonacci + after
#         fibonacci = after
#         after = aux
#         counter += 1

#Ex 03
secret_word = 'python'
discovered_letter = ['_'] * len(secret_word)
tries = 6

while tries > 0 and '_' in discovered_letter:
    print('Palavra', ''.join(discovered_letter))
    letter = input('Digite uma letra: ').lower()

    if letter in secret_word:
        for idx, secret_letter in enumerate(secret_word):
            if letter == secret_letter:
                discovered_letter[idx] = letter
            
        print('Boa! Você acertou uma letra.')
    else: 
        tries -= 1
        print(f'Errou! Você tem {tries} tentativas restantes.')

if '_' not in discovered_letter:
    print('Parabéns! Você advinhou a palavra:', secret_word)
else: 
    print('Você perdeu! A palavra secreta era:', secret_word)