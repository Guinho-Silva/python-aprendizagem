'''
4) Faça um programa que tenha uma função chamada "maior()", que receba vários parâmetros com valores inteiros

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(* num):
   cont = mai = 0

   print('\nAnalisando...')

   for valores in num:
        print(f'{valores} ',end='', flush=True)

        if cont == 0:
            mai = valores

        if valores > mai:
            mai = valores 
        
        cont +=1
   print(f'\nO maior valor foi {mai}')

maior(2, 1, 4, 8, 8, 20)
maior(3,4,5,7)
maior(4,50,33)
maior(2,6)
maior(7)
maior()

'''resposta = ''

ListaNum = list()

while True:
    NumDigitado = int(input('Digite um número: '))
    
    ListaNum.append(NumDigitado)


    if len(ListaNum) == 1:
        mai = men = NumDigitado

    else:
        mai, men = maior(NumDigitado,mai,men)

    while True:
        resposta = str(input('Quer continuar [S/N]? ')).upper()

        if resposta in 'SN':
            break
        print('Resposta inválida! Digite "S" para continuar e "N" para encerrar.')

    if resposta == 'N':
        break

print(ListaNum)

print(f'Maior: {mai}')
print(f'Menor: {men}')
'''