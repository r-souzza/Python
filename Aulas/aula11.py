# AULA 11: Aula sobre precedência entre os operadores aritméticos (prioridade de cada operador)

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + - 

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)


conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)


# Exemplo de como uma variável pode ter seu valor alterado
conta_1 = 1 + 1 ** 5 + 5
conta_1 = 'Variável alterada'
print(conta_1)