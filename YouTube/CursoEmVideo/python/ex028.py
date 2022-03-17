from random import randint
computador = randint(1, 3)
print('Pensei no número...')
nome = (input('Escolha seu nick: '))
print('-=-' * 20)
print('A máquina ira pensar em um número de 1 até 3!')
print('-=-' * 20)
jogador = int(input('- Em que número eu pensei? '))

if jogador == computador:
    print('- Parbéns por me derrotar {}, eu escolhi o número {}' .format(nome, computador))
else:
    print('- Eu ganhei {}, eu escolhi o número {}' .format(nome, computador))