dis = int(input('Digite a distancia da sua viagem: '))
if dis >= 200:
    print('Você está em uma viagem promocial! Sua distancia: {}' .format(dis))
    res = dis * 0.45
else:
    print('Sua distancia: {}' .format(dis))
    res = dis * 0.50
print('O valor gasto nesta viagem é: R${:.2f}' .format(res))
