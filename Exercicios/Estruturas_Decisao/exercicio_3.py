# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite (M)asculino ou (F)eminino: ").upper()
# UPPER() - para tornar a letra maiúscula caso o usuário digite minúscula

# Verificando a letra inserida

if letra == 'M':
    print('Masculino')

elif letra == 'F':
    print('Feminino')

else:
   print('Inválido')