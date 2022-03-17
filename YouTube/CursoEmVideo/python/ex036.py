casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiameno: '))
prestacao = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}' .format(casa, anos, prestacao))

if prestacao >= (30 / 100) * salario:
    print('Emprestimo poder ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO')
