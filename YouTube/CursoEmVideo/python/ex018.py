from math import radians, sin, cos, tan
an = float(input('Digite um angulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print('-' * 15)
print('Seno: {:.2f}' .format(seno))
print('Cosseno: {:.2f}' .format(cosseno))
print('Tangente: {:.2f}' .format(tangente))
print('-' * 15)