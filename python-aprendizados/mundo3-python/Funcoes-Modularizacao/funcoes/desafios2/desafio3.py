'''
3)Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
'''

def ficha(nome='',gols= 0):
    listaJogador = []

    listaJogador.append(nome)
    listaJogador.append(gols)
    return listaJogador

nomeJogador = str(input('Nome do jogador: '))

QtdeGols = input('Gols marcados: ')

if QtdeGols == '':
    QtdeGols = 0
else:
    QtdeGols = int(QtdeGols)



resposta = ficha(nomeJogador,QtdeGols)


print(f'O jogador {resposta[0]} marcou {resposta[1]} gols')