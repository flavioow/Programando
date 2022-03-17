n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))

if n1 > n2:
    print('O número maior é {}, o menor é {}!' .format(n1, n2))
elif n1 == n2:
    print('Os números são iguais!')
else:
    print('O número maior é {}, o menor é {}!' .format(n2,n1))
