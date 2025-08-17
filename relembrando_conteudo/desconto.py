#Verificar se um desconto é dado a um cliente
itens = int(input('Insira a quantidade de itens pertencentes a compra: '))
value = float(input('Insira o valor final da compra: '))
discount = (itens >= 10) or (value >= 100)

print(f'O desconto foi aplicado? {discount}')