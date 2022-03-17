d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos Km rodados? '))
p = float(input('Quanto custou o carro? '))
a = int(input('Qual é o ano do carro (os 2 ultimos digitos depois do ano 2000)? '))

v = ((d * 25) + (k * 0.3) + (p + (p * 2 / 100)) + (a + (a * 0.5 / 100)))

print('O total a pagar é: R${:.2f}' .format(v))
