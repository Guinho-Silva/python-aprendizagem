'''
4)Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.

ex: leiaint('Digite um n')
'''
def leiaint(msg):
    valorDigitado = False

    valor = 0

    while True:
        num = str(input(msg))

        if num.isnumeric():
            valor = int(num)
            valorDigitado = True
        else:
            print('Número inválido! Digite um número inteiro')
        if valorDigitado:
            break
    return valor

n1 = leiaint('Digite um número: ')

print(f'Você digitou o número {n1}')