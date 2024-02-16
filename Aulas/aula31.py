# AULA 31: Aula sobre ID

"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

"""

# v1 = 'a'
# v2 = 'a'

# print(id(v1)) # Verificar o id de uma variável
# print(id(v2)) # O id das duas variáveis são iguais pois as duas possuem o mesmo valor

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')