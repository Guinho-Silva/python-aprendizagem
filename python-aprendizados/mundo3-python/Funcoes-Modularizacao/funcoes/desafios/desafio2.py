'''
2) Faça um programa que tenha uma função chamada "esreva(), que receba um texto qualquer como parâmetro e  mostre uma mensagem com tamanho adaptável"'''

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

escreva('Iago Silva')