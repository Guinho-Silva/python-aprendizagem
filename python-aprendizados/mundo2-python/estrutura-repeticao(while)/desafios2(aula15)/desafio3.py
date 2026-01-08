'''3)Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder. Mostre o total de vitórias consecutivas no final do jogo'''


import random

vitorias = 0

while True:
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()
    jogador = int(input('Digite um número: '))
    computador = random.randint(0, 10)

    soma = jogador + computador

    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    print(f'Você jogou {jogador} e o computador {computador}. Total = {soma}')

    if escolha == resultado:
        print('Você ganhou!')
        vitorias += 1
        print('Vamos jogar novamente...\n')
    else:
        print('Você perdeu!')
        break

print(f'Vitórias consecutivas: {vitorias}')
