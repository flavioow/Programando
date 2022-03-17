l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l * a
print('Sua parede tem as dimenções: {} X {} e a sua área é de {}m²' .format(l, a, ar))
t = ar / 2
print('Para pintar está parede, você precisará de {:.3f} litros de tinta' .format(t))
