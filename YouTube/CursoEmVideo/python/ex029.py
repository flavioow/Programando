vel = int(input('Qual é a sua velocidade? '))
if vel <= 80:
    print('Tenha um bom dia')
else:
    multa = (vel - 80) * 7
    print('Você levou uma multa de {:.2f}R$!' .format(multa))
