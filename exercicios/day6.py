# Ex 01
# guests = ['Jolteon', 'Umbreon', 'Espeon', 'Leafeon', 'Sylveon']

# for index, guest in enumerate(guests):
#     print(f'{guest} seja bem vindo! Você é o nosso {index +1}º convidado a chegar')

# Ex 02
# inputed_numbers = input('Digite números separados pos espaço: ')
# numbers = [float(num) for num in inputed_numbers.split()]

# biggest = 0
# lesser = numbers[0]
# sum = 0
# media = 0

# for index, number in enumerate(numbers): 
#     if number > biggest:
#         biggest = number

#     if lesser > number:
#         lesser = number
    
#     sum += number

#     if index == (len(numbers) - 1):
#         media = sum / len(numbers)

# print(f'O mair número é: {biggest}')
# print(f'O menor número é: {lesser}')
# print(f'A soma de todos os números é de: {sum}')
# print(f'A media entre os números é de: {media}')

# Ex 03 isalpha() .itens()
# phrase = input('Digite uma frase: ').lower()
# letters = {}

# for letter in phrase:
#     if letter.isalpha():
#         if letter in letters :
#             letters[letter] += 1
#         else:
#             letters[letter] = 1
        
# for letter, count in letters.items():
#     print(f"A letra '{letter}', apareceu {count} vezes")

# Ex 04
# numbers = input('Insira uma lista de números separados por espaço: ').split()
# growing_order = []

# for i in range(len(numbers)):
#     biggest = max(numbers)
#     numbers.remove(biggest)
#     growing_order.append(biggest)


# print('Orden crescente:', growing_order)

# growing_order.reverse()

# print('Orden decrescente:', growing_order)

# Ex 05
# month = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# month_number = int(input('Digite um número entre 1 e 12: '))

# print(f'O mês correspondente ao número que você digitou foi {month[month_number - 1]}')

# Extra 01
# tasks = []

# while True:
#     print('=========Lista de Tarefas=========')
#     print('1 | Adicionar Tarefa')
#     print('2 | Remover Tarefa')
#     print('3 | Listar Tarefas')
#     print('4 | Sair')

#     option = int(input('Insira o número da ação que deseja executar: '))

#     if option == 1:
#         new_task = input('Insira a nova tarefa: ')
#         tasks.append(new_task)
#     elif option == 2:
#         new_task = input('Qual tarefa será removida: ')
#         tasks.remove(new_task)
#     elif option == 3:
#         print('Essas são suas tarefas!')

#         if len(tasks) == 0:
#             print('Você não tem nenhuma tarefa no momento.')

#         for task in tasks:
#             print(f' - {task}')
#     elif option == 4:
#         break

#     else:
#         print('A ação desejada não existe, por favor insira uma ação valida')

# Extra 02
# grades = []

# while True:
#     user_input = input('Digite o valor da nota (Ou "Sair"): ')

#     if user_input == 'Sair':
#         print('Saindo...')
#         break

#     new_grade = float(user_input)

#     if 0.0 <= new_grade <= 25.0 : 
#         grades.append(new_grade)
#     else:
#         print('Insira uma nota valida.')

# if grades != []:

#     biggest_grade = max(grades)
#     lesser_grade = min(grades)
#     average_grade = sum(grades) / len(grades)
#     above_average_grades = [grade for grade in grades if grade >= 15]

#     print(f'\nA maior nota foi: {biggest_grade}')
#     print(f'A menor nota foi: {lesser_grade}')
#     print(f'A media das notas foi: {average_grade}')
#     print(f'As notas acima da média foram {above_average_grades}')

# Extra 03
# Usando o join()
# text = input('Digite um texto: ').lower()

# word = []
# words = {}
# delimiter = ''

# for letter in text:
#     if letter != ' ':
#         word.append(letter)
#     else:
#         user_word = delimiter.join(word)
#         word = []

#         if user_word in words:
#             words[user_word] += 1
#         else:
#             words[user_word] = 1
    

# for word, contagem in words.items():
#     print(f'A palavra "{word}" aparece {contagem} vez(es).')

# Usando o split()
# text = input('Digite um texto: ').lower()
# words = text.split()
# words_counted = {}


# for word in words:    
#     if word in words_counted:
#         words_counted[word] += 1
#     else:
#         words_counted[word] = 1
    

# for word, conting in words_counted.items():
#     print(f'A palavra "{word}" aparece {conting} vez(es).')