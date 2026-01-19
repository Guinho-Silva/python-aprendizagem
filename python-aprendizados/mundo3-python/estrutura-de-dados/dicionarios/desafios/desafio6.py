'''6) Aprimore o desafio 4 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador'''

ListaCadastro = list()

ContGols = 1

resposta = ''

while True:
    Dicionario = dict()

    Dicionario['NomeJogador'] = str(input('Nome: '))
    Dicionario['NumPartidas'] = int(input('Quantidade de Partidas: '))
    Dicionario['NumGols'] = []
    
    for partidas in range(Dicionario['NumPartidas']):
        Gols = int(input(f'N° de Gols na {partidas + 1}° : '))
        Dicionario['NumGols'].append(Gols)
    ListaCadastro.append(Dicionario)
    Dicionario['TotGols'] = sum(Dicionario['NumGols'])
  
    while True:
        resposta = str(input('Quer continuar [S/N]? ')).upper()

        if resposta in 'SN':
            break
        print('Resposta inválida! Digite "S" para continuar e "N" para encerrar: ')

    if resposta == 'N':
        break


print('-'*30)
print()

print(f'{"ID.":<4}{"Nome":<10}{"Gols":<10}{"Total":>12}')
print()
for i, jogador in enumerate(ListaCadastro):
    print(f'{i + 1:<4}{jogador["NomeJogador"]:<10}{str(jogador["NumGols"]):<10}{jogador["TotGols"]:>12}')

while True:
    dados = int(input('Mostrar os dados de qual jogador? (Digite 999 para encerrar): '))

    if dados == 999:
        print('Encerrando...')
        break

    dados -= 1

    if dados >= len(ListaCadastro) or dados < 0:
        print('ID inválido! Tente novamente.')
        continue

    jogador = ListaCadastro[dados]

    print(f'\n--- Dados do Jogador {jogador["NomeJogador"]} ---')
    for i, gols in enumerate(jogador['NumGols']):
        print(f'  Na partida {i + 1} fez {gols} gols')
    print(f'Total de gols: {jogador["TotGols"]}\n')
