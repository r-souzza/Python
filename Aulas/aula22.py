# AULA 22: Operador lógico OR

'''
and (e) or (ou) not (não)

or - Qualquer condição vcerdadeira avalia
toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro,
a expressão inteira será avaliada naquele valor.

São considerados falsy 
0 0.0 '' False
Também existe o tipo None que é
usado para representar um não valor

'''

# Exemplo da LÓGICA do operador lógico OR

entrada = input('[E]ntrada [Sair]: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')

# Avaliação de curto circuito[
# print(True or False)
# print(True or False or 0)
# print(True or False or 0 or 'abc' or True)

