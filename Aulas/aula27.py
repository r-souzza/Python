# AULA 27: Fatiamento de strings e função len

"""
 Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: a função len retorna a quantidade
de caracteres da string

"""

variavel = 'Ola mundo'

print(variavel[4:]) # [onde inicia : onde para]

print(len(variavel)) # função len é utilizada para contar caracteres

print(variavel[0:9:2]) # [onde inicia : onde para : quantidade de passos]

print(variavel[::-1]) # quantidade de passos negativos inverte a string

