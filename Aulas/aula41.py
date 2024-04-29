# AULA 41

""" while / else """

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else: # Else é executado quando o while foir completado
    print('Não encontrei um espaço na string')
print('Fora do while, else não será executado')