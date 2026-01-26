'''
2)Crie um programa que tenha uma função chamada fatorial() que receba parâmetros: o primeiro que indique o número a calcular e o outro chamada show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo do cálculo do fatorial
'''

def fatorial(num = 1, Show=False):
    f = 1
    for valor in range(num, 0, -1):
         
        f *= valor
        if Show:
            print(valor, end=' x ' if valor > 1 else ' = ')

       
    return f


n = int(input('Digite um valor: '))

print(f'{fatorial(n, Show=True)}')

