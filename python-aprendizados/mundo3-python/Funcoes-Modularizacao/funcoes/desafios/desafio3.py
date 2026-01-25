'''
3) Faça um programa que tenha um função chamada "contador()", que receba três parâmetros: Inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c)Uma contagem personalizada
'''
from time import sleep
def contador(inicio, fim, passo):

    if passo == 0:
        print('Valor inválido!Por tanto o passo será igual a 1')

        passo = 1

 

    if inicio < fim:

        passo = passo

        for valores in range(inicio, fim + 1, passo): 
            print(valores, end=' ', flush=True)
            sleep(0.5)
        print('\n')

        
        

    else:
        passo = -passo
        for inverso in range(inicio, fim - 1, passo):

            print(inverso, end=' ', flush=True)
            sleep(0.5)

print('Contagem de 1 a 10: ')
   
contador(1, 10, 1)

print()

print('Contagem regressiva de 10 a 0, de 2 em 2: ')
        
contador(10, 0, 2)
print('\n')

inicio = int(input('inicio: '))

fim = int(input('Fim: '))

passo = int(input('Passo: '))

contador(inicio, fim, passo)