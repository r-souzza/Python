# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')

if letra.isalpha(): # Verificando se o valor digitado é uma letra

    if letra == 'a' or letra == 'e' or letra == 'i' or \
    letra == 'o' or letra == 'u':
        print(f'A letra {letra} é uma vogal.')

    else:
        print(f'A letra {letra} é uma consoante.')

else: # Caso o valor digitado não seja uma letra
    print(f'O valor informado: {letra}, não é uma letra.')