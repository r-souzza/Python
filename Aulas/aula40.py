# AULA 40: Calculadora

""" Calculadora com while """

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None


    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue


    print('Realizando a sua conta, confira o resultado abaixo:')    
    if operador == '+':
        print (num_1 + num_2)

    elif operador == '-':
        print (num_1 - num_2)

    elif operador == '/':
        print (num_1 / num_2)
    
    elif operador == '*':
        print (num_1 * num_2)

    else:
        ...



    sair = input('Deseja sair? [S]im').lower().startswith('s')
    # sair.upper() # .upper() para letra maíuscula , .lower() para letra mínuscula
    # sair = sair.startswith('s') - .startswith() = "começa com"

