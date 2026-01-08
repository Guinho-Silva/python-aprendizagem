n1 = int(input('Digite um valor: '))

n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('Este valor {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('Este valor {} é maior que'.format(n2, n1))
else:
    print('Os dois valores são iguais.')

'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
'''