# AULA 28: Exercício

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios."

"""


nome = input('Digite seu nome: ')
nome_invertido = (nome[::-1])
n = (len(nome))
primeira_letra = (len(nome[0]))
#idade = input('Digite sua idade: ')


print(f'Seu nome é {nome}')
print(f'Seu nome invertido é {nome_invertido}')
print(f'Seu nome tem {n} letras')
print(f'A primeira letra do seu nome é {primeira_letra}')


