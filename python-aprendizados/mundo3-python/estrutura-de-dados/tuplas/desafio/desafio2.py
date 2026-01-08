'''2) Crie uma tupla preenchida com os 20 colocados do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados

B) Os últimos 4 colocados da tabela

c) Uma lista com os times em ordem alfabética

d) Em que posição na tabela o time da Chapecoense.'''

ColocTimes =  ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Red Bull Bragantino', 'Atlético-MG', 'Santos', 'Corinthians','Vasco', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')

print(f'Os 5 primeiros colocados são: {ColocTimes[:5]}')

print(f'Os últimos 4 colocados da tabela são: {ColocTimes[16:]}')

print(f'O São Paulo esta na posição {ColocTimes.index('São Paulo') + 1}')