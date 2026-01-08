'''7) Faça um programa que leia um número inteiro e diga se ele é não é um número primo.
'''


n1 = int(input('Digite um valor: '))

if n1 <= 1:
    print('Não é primo!')
else:
    for c in range(2, int(n1**0.5) + 1):
        if n1 % c == 0:
            print('Não é primo')
            break
    else:
        print('É primo')

print('Fim do programa!')
