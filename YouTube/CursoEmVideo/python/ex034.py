salario = int(input('Qual é o seu salário? '))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print('Seu salário de {}, passou a ser {}, com15% de aumento' .format(salario, aumento))
else:
    aumento = salario + (salario * 10 / 100)
    print('Seu salário de {}, passou a ser {}, com 10% de aumento' .format(salario, aumento))
