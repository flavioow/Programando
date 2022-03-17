frase = str(input('Digite uma FRASE: ')).upper()
print('A letra "A" apareceu {} na frase.' .format(frase.count('A')))
print('A letra "A" apareceu pela primeira vez na {} posição.' .format(frase.find('A')+1))
print('A letra "A" apareceu pela última vez na {} posição.' .format(frase.rfind('A')+1))
