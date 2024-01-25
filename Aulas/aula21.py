# AULA 21: Operador lógico AND

'''
and (e) or (ou) not (não)

and - Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor

São considerados falsy 
0 0.0 '' False
Também existe o tipo None que é
usado para representar um não valor

'''

# Exemplo da LÓGICA do operador lógico AND

entrada = input('[E]ntrada [Sair]: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')


# Avaliação de curto circuito
# print(True and True and True) 
# print(True and False and True)