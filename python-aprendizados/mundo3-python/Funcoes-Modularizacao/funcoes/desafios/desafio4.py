'''
4) Faça um programa que tenha uma função chamada "maior()", que receba vários parâmetros com valores inteiros

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(num, mai, men):
   
    if num > mai:
        mai = num 
    
    if num < men:
        men = num
    
    return mai, men


resposta = ''

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