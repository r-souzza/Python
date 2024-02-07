# AULA 30: Variáveis, constantes e complexidade do código

"""
CONSTANTE = 'Variáveis' que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade, blocos dentro de outros blocos (ruim)

"""

velocidade = 62 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

# Costuma utilizar apenas letras maiusculas em CONSTANTES

RADAR_1 = 61 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_car_pass_radar_1 = velocidade > RADAR_1

carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1

if vel_car_pass_radar_1:
    print('Velocidade do carro acima do radar 1')
    

if carro_multado_radar_1 and vel_car_pass_radar_1:
        print("Carro multado em radar 1")