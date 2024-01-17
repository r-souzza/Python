# AULA 15: Aula sobre a função input

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')
print(f'O seu nome é {nome=}') # Mostrar o nome da variável e o valor da variável


# A função input coleta apenas string, caso precise realizar um cálculo é necessário converter o tipo da variável
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

# OU

# numero_1 = input('Digite um número: ')
# int_numero_1 = int(numero_1)

# numero_2 = input('Digite outro número: ')
# int_numero_2 = int(numero_2)


print(f'A soma dos números é: {numero_1 + numero_2}')