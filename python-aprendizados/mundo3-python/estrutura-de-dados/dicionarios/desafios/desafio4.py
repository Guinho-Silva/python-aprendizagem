'''
4) Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato
'''
listaDados = list()

ContGols = 1
while True:
    DadosJogadores = dict()
    DadosJogadores['Nome'] = str(input('Nome: '))
    DadosJogadores['NumPartida'] = int(input('N° de Partidas: '))
    DadosJogadores['NumGols'] = []
    DadosJogadores['TotGols'] = sum(DadosJogadores['NumGols'])
    for partidas in range(DadosJogadores['NumPartida']):
        Gols = int(input(f'N° de Gols na {partidas + 1}° : '))
        DadosJogadores['NumGols'].append(Gols)
    listaDados.append(DadosJogadores)
    DadosJogadores['TotGols'] = sum(DadosJogadores['NumGols'])

    break
print('-='*30)
print()
print(listaDados)
print('-'*30)

print(f'Nome do jogador: {DadosJogadores["Nome"]}')
print(f'O jogador {DadosJogadores["Nome"]} fez {DadosJogadores["NumGols"]} gols ')
print(f'O {DadosJogadores["Nome"]} fez {DadosJogadores["TotGols"]} gols')
print('-='*30)

for jogo in range(DadosJogadores['NumPartida']):
    print(f'Na {jogo + 1}° Partida, fez {DadosJogadores["NumGols"][jogo]} gol(s)')