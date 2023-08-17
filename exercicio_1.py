# Faça um Programa que peça dois números e imprima o maior deles.

# SOLICITANDO OS NÚMEROS

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

# COMPARANDO OS NÚMEROS E EXIBINDO O RESULTADO

if num_1 > num_2:
    print(f'O número {num_1} é maior que o número {num_2}')
else:
    print(f'O número {num_2} é maior que o número {num_1}')
