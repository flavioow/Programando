import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
# Dica - hi = (co ** 2 + ca **2) ** (1/2)
print('A hipotenusa vai medir {:.3f}' .format(hi))
