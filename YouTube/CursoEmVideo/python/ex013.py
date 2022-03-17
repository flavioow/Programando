funx = input('Qual é o nome do funcionário? ')
ax = float(input('Quanto ganha este funcionário? '))
rx = ax + (ax * 73 / 100)

funy = input('Qual é o nome de outro funcionário? ')
ay = float(input('Quanto ganha este funcionário? '))
ry = ay + (ay * 73 / 100)

print('O funcionário {} ganhava R${:.2f}, depois de um aumento de 73%, passa a receber R${:.2f} ' .format(funx, ax, rx))
print('O funcionário {} ganhava R${:.2f}, depois de um aumento de 73%, passa a receber R${:.2f} ' .format(funy, ay, ry))
