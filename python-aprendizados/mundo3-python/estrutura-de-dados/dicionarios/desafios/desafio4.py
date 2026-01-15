'''
4) Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato
'''
listaDados = list()

while True:
    DadosJogadores = dict()

    DadosJogadores['Nome'] = str(input('Nome: '))
    DadosJogadores['NumPartida'] = int(input('N° de Partidas: '))
    DadosJogadores['NumGols'] = str(input('N° de Gols: '))
    listaDados.append(DadosJogadores)

    break
print(listaDados)