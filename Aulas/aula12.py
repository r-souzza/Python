# AULA 12: Exercício - Cálculo IMC


nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

print(f'{nome} tem {altura} de altura, pesa {peso} e seu IMC é {imc:.2f}')