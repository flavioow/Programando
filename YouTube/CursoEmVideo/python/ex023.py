num = int(input('Digite um número natural (até milhar): '))
n = str(num)
print("""
Analisando o número: {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""" .format(num, n[3],n[2],n[1],n[0]))
