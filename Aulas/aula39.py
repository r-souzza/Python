# AULA 36: Exercício guiado com while

"""
Iterando strings com while

"""
# Inserir um caracter entre cada índice (letra) de um nome

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)

