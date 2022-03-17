a =  float(input('Qual é o preço do produto? R$'))
d = a - (a * 23 / 100)
print('O produto que custava R${:.2f}, na promoção de 23% de desconto vai custar: R${:.2f}' .format(a, d))
