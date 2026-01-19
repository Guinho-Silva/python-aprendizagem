'''
3) Faça um programa que tenha um função chamada "contador()", que receba três parâmetros: Inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c)Uma contagem personalizada
'''
from time import sleep
def contador():
    print('Contagem de  1 a 10')
    print()
    for valores in range(1, 11,1): 
        print(valores, end=' ', flush=True)
        sleep(0.5)
    print('\n')

    print('Contagem regressiva de 10 a 0, de 2 em 2:')
    print()
    for inverso in range(10, 0, -2):
        print(inverso, end=' ', flush=True)
        sleep(0.5)


contador()
print('\n')
inicio = int(input('inicio: '))

fim = int(input('Fim: '))

passo = int(input('Passo: '))

if passo == 0:
    print('Valor inválido!Por tanto o passo será igual a 1')

    passo = 1
else:
    if inicio > fim:
        passo = -passo

print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

for valor in range(inicio,fim,passo):
    
    print(valor, end=' ')