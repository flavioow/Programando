import random
aa = str(input('Nome do primeiro aluno(a): '))
ab = str(input('Nome do segundo aluno(a): '))
ac = str(input('Nome do terceiro aluno(a): '))
ad = str(input('Nome do quarto aluno(a): '))
lista = [aa, ab, ac, ad]
random.shuffle(lista)

print('A ordem escolhida é: ')
print(lista)
