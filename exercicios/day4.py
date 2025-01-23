# # Ex 01
# number = int(input('Insira um número: '))

# if number > 0:
#     print('O número inserido é positivo')
# elif number < 0:
#     print('O número inserido é negativo')
# else:
#     print('O número inserido é 0')

# # Ex 02 
# calculation_number_a = float(input('Insira um número: '))
# calculation_number_b = float(input('Insira outro número: '))
# calculation_operator = str(input('Insira um operador matemático: '))

# if calculation_operator == '+':
#     print(calculation_number_a + calculation_number_b)
# elif calculation_operator == '-':
#     print(calculation_number_a - calculation_number_b)
# elif calculation_operator == '*':
#     print(calculation_number_a * calculation_number_b)
# elif calculation_operator == '/':
#     if calculation_number_b != 0:
#         print(calculation_number_a / calculation_number_b)
#     else:
#         print('Não é possível dividir por 0')
# else:
#     print('Esta operação não pode ser realizada')

# Ex 03
# user_age = int(input('Insira sua idade: '))

# if user_age < 12:
#     print('Você é criança')
# elif user_age < 17:
#     print('Vocé é adolecente')
# elif user_age < 59: 
#     print('Você é adulto')
# elif user_age > 59:
#     print('Você é idoso')
# else: 
#     print('Idade invalida')

# Ex 04
# year = int(input('Insira um ano: '))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('Este é um ano bissexto')
# else:
#     print('Este não é um ano bissexto')

# Ex 05
# withdrawal_value = int(input('Insira o valor a ser sacado: R$'))
# rest_value = withdrawal_value

# if withdrawal_value <= 1 or withdrawal_value == 3:
#     print('Valor inválido para o saque')
# else:
#     bills_100 = rest_value // 100
#     rest_value %= 100

#     bills_50 = rest_value // 50
#     rest_value %= 50

#     bills_20 = rest_value // 20
#     rest_value %= 20

#     bills_10 = rest_value // 10
#     rest_value %= 10

#     if rest_value == 8:
#         bills_5 = 0
#         bills_2 = rest_value // 2
#         rest_value %= 2
#     else:
#         bills_5 = rest_value // 5
#         rest_value %= 5

#         bills_2 = rest_value // 2
#         rest_value %= 2

#     if rest_value != 1:
#         print('O saque de R$', withdrawal_value, 'reais, foi feito em:')
#         if bills_100 > 0:
#             print(bills_100, 'notas de 100')
#         if bills_50 > 0:
#             print(bills_50, 'notas de 50')
#         if bills_20 > 0:
#             print(bills_20, 'notas de 20')
#         if bills_10 > 0:
#             print(bills_10, 'notas de 10')
#         if bills_5 > 0:
#             print(bills_5, 'notas de 5')
#         if bills_2 > 0:
#             print(bills_2, 'notas de 2')
#     else:
#         print('Não foi possivel realizar o saque com esse valor')

# Extra 01
# loan = float(input('Insira do emprestimo desejado: R$'))
# income = float(input('Insira o valor de sua renda mensal: R$'))
# tranche = int(input('Insira em quantas parcelas deseja pagar o emprestimo: '))

# if (loan / tranche) <= (income * 0.3):
#     print('O imprestimo foi aprovado!')
# else:
#     print('O imprestimo não foi aprovado!')

# Extra 03
distancy = float(input('Digite de quantos Km serão a viagem: Km'))
base_fare = 4
add = 0.25

total_value = distancy * add + base_fare
print(f'O valor total da corrida foi de: R${total_value:.2f}')

