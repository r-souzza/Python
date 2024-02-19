# AULA 32: Exercícios 

"""
Faça um programa que peça ao usuário digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro.

"""

# num = input("Digite um número inteiro: ")

# if num.isdigit(): # Checa se o valor digitado é um número/dígito
#     num = int(num)

#     if num % 2 == 0:
#         print(f'o número {num} é par')

#     else:
#         print(f'O número {num} é ímpar.')

# else:
#     print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada.
Ex: Bom dia 0 - 11, Boa tarde 12 - 17, Boa noite 18 - 23

"""

hora = input("Digite a hora atual em números inteiros: ")

if hora.isdigit():
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')

    elif hora >= 12 and hora <=17:
        print('Boa tarde!')

    elif hora >=18 and hora <=23:
        print('Boa noite!')

    else:
        print('Não conheço a hora informada.')

else:
    print('Você não digitou um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande.

"""

# nome = input("Digite seu primeiro nome: ")
# tamanho_nome = len(nome)

# if tamanho_nome > 1:

#     if len(nome) <= 4:
#         print("Seu nome é curto.")

#     elif len(nome) == 5 or len(nome) == 6:
#         print("Seu nome é normal.")

#     else:
#         print('Seu nome é muito grande.')

# else:
#     print('Digite mais de uma letra.')



