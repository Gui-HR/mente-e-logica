print('Digite qual operação você quer realizar: Adição - Subtração - Divisão - Multiplicação:')
operation = input('Insira a operação:').lower()
number_a = float(input('Insira um número desejado, para realizar a operação:'))
number_b = float(input('Insira o segundo número desejado, para realizar a operação:'))
result = 0

if operation == 'soma':
    result = number_a + number_b
elif operation == 'subtração':
    result = number_a - number_b
elif operation == 'multiplicação':
    result = number_a * number_b
elif operation == 'divisão':
    result = number_a / number_b

print(f'O resultado da {operation} de {number_a} e {number_b} foi: {result}')

