# Ex 01
# num_a = float(input('Digite um número: '))
# num_b = float(input('Digite outro número: '))
# operation = input('Escolha qual será a operação matematica realizada (+, -, *, /): ')

# def plus(num_a, num_b):
#     return num_a + num_b

# def minus(num_a, num_b):
#     return num_a - num_b

# def multiplication(num_a, num_b):
#     return num_a * num_b

# def division(num_a, num_b):
#     return num_a / num_b

# if operation == '+':
#     result = plus(num_a, num_b)
# elif operation == '-':
#     result = minus(num_a, num_b)
# elif operation == '*':
#     result = multiplication(num_a, num_b)
# elif operation == '/':
#     result = division(num_a, num_b)

# print(result)

#Ex 02
# number = int(input('Insira um número inteito para saber se ele é ou não um número primo: '))

# def is_prime_number(num):
#     if num <= 1:
#         return False

#     for i in range(2, number):
#         if number % i == 0:
#             return False
    
#     return True

# if is_prime_number(number):
#     print(f'{number} é um número primo')
# else: 
#     print(f'{number} não é um número primo')

#Ex 03
# print('------ Conversor de Temperatura ------\n')

# temperature = float(input('Informe a temperatura que deseja converter (apenas o número): '))
# unit = input('Informe qual a unidade da temperatura informada acima (C, K, F): ').upper()

# def celcius_to_fahrenheit(temp, unit):
#     if unit == 'C':
#         return (temp * 9/5) + 32
#     elif unit == 'F':
#         return (temp - 32) * 5/9

# def celcius_to_kelvin(temp, unit):
#     if unit == 'C':
#         return temp + 273.15
#     elif unit == 'K':
#         return temp - 273.15

# def kelvin_to_fahrenheit(temp, unit):
#     if unit == 'K':
#         return (temp - 273.15) * 9/5 + 32
#     elif unit == 'F':
#         return (temp - 32) * 5/9 + 273.15

# if unit == 'C':
#     celcius = temperature
#     fahrenheit = celcius_to_fahrenheit(temperature, unit)
#     kelvin = celcius_to_kelvin(temperature, unit)
# elif unit == 'F':
#     fahrenheit = temperature
#     celcius = celcius_to_fahrenheit(temperature, unit)
#     kelvin = kelvin_to_fahrenheit(temperature, unit)
# elif unit == 'K':
#     kelvin = temperature
#     celcius = celcius_to_kelvin(temperature, unit)
#     fahrenheit = kelvin_to_fahrenheit(temperature, unit)

# print(f'{celcius:.2f} C°')
# print(f'{kelvin:.2f} K°')
# print(f'{fahrenheit:.2f} F°')

# Ex 04
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# number = int(input('Insira um número para descobrir seu fatorial: '))
# result = factorial(number)

# print(f'O fatorial de {number} é: {result}.')

# Extra 01
# import random
# import string

# def validate_data(password_lenght):
#     if password_lenght.isdigit():
#         password_lenght = int(password_lenght)
#         if password_lenght >= 8 and password_lenght <= 12:
#             return password_lenght
            
#     print('O valor informado não aceito. Sua senha atual tera 8 digitos.')
#     return 8

# def generate_password(length):
#     validated_password_length = validate_data(length)
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(validated_password_length))
#     return password

# password_lenght = input('Insira um número inteiro entre 8 12 para gerar uma nova senha com o tamanho especificado: ')
# ""
# new_password = generate_password(password_lenght)

# print(f'Sua nova senha é {new_password}')

# Extra 03 Palíndromo
def is_palindrome(text):
    tester_text = text[::-1].replace(' ', '')
    
    if tester_text == text.replace(' ', ''):
        print(f'"{text}" é um palíndromo')
        return
    
    print(f'"{text}" não é um palíndromo')

user_text = input('Insira uma palavra ou frase para descobri se é um palíndromo: ').lower()

is_palindrome(user_text)


