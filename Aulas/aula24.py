# AULA 24: Operadores in e not in

# Operadores in e not in
# Strings são iteráveis (posso acessar cada elemento, índices)
#  0 1 2 3 4
#  R O G E R
# -5-4-3-2-1

# nome = 'Roger'

# print(nome[1])
# print(nome[-5])

# print('r' in nome)
# print('z' not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')



