'''1) Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep

Contador = 10

for c in range (Contador, 0, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!!!')