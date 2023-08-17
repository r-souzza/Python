# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# SOLICITANDO OS NÚMEROS

num = input('Digite um número: ')
num = int(num)

# VERIFICANDO SE O NÚMERO É POSITTIVO OU NEGATIVO

if num >= 0:
    print('O número informado é positivo.')

elif num < 0:
    print('O número informado é negativo.')

else:
    print('Valor não reconhecido.')