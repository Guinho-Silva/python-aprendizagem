'''
4) Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado ou não na lista
'''

continuar = ''

ValoresLidos = []

while True:
    valores = int(input('Digite um valor: '))

    ValoresLidos.append(valores)

    continuar = input('Quer continuar?[S/N]: ').upper()

    if continuar == 'N':
        break

ValoresLidos.sort(reverse=True)

print(f'Foram digitados: {len(ValoresLidos)} valores!')
print(f'Os valores em forma decrescente é: {ValoresLidos}')

if 5 not in ValoresLidos:
    print('O valor 5 não foi digitado!')

else:
    print('O valor 5 foi digitado!')