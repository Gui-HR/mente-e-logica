# Ex 01
bread = 3.5
milk = 4.2
coffee = 2.8

purchase = bread + milk + coffee
money = 20
change = money - purchase

print('Valor da compra:', purchase)
print('Troco da compra:', change)

# Ex 02
grade_rate = 8.5
frequency = 80

approval = grade_rate >= 7.0 and frequency >= 75

print('O estudante foi aprovado?', approval)

# Ex 03
itens_quantity = 8
total_value = 120

discount = itens_quantity >= 10 or total_value > 100

print('O cliente tem direito a desconto?', discount)

# Ex 04
input_password = 'abcd1234'
correct_password = 'abcd1234'
user_blocked = False

allow_access = correct_password == input_password and not user_blocked

print('Acesso concedido?', allow_access)

# Ex 04
bill = 150
friends = 3

value_per_capita = bill // friends

exact_division = (bill % friends) == 0

print('Quando cada um deve pagar?', value_per_capita)
print('A divisão é exata?', exact_division)

# Extra 01 
user_age = 20
movie_age = 16
can_watch = not user_age <= movie_age

print('O usuário pode ver o filme? ', can_watch)

# Extra 02
user_height = float(input('Digite sua altura em metros: '))
user_weight = float(input('Digite seu peso em quilos: '))
user_imc = user_weight / (user_height ** 2)
ideal_weight = user_imc > 18.5 and user_imc < 24.9

print('Seu IMC é de: ', user_imc)
print('Seu IMC é ideal? ', ideal_weight)

# Extra 03 
number = int(input('Insira um número inteiro: '))
is_even = number % 2 == 0

print('O número é par? ', is_even)