'''
5) Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em um lista composta
'''
from random import randint 
from time import sleep

Palpites = []

jogos = []
cont = 0

QtdJogos = int(input('Quantas jogos você quer gerar?: '))

tot = 1

while tot <= QtdJogos:
    cont = 0
    while True:
        num = randint(1, 60)

        if num not in Palpites:
            Palpites.append(num)
            cont += 1
        if cont >= 6:
            break


    Palpites.sort()
    jogos.append(Palpites[:])
    Palpites.clear()

    tot += 1
for i, lista in enumerate(jogos):
    print(f'Jogo {i+1}: {lista}')
    sleep(1)