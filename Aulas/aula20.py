# AULA 20: EXERCÍCIO - Solicite dois numeroes o informe qual é o maior deles

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))


if numero1 > numero2:
    print(f'O número {numero1} é maior que o número {numero2}')

elif numero2 > numero1:
    print(f'O número {numero2} é maior que o número {numero1}')

else:
    print('Os dois números  inseridos são iguais.')