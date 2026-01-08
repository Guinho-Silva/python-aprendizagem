"""1) Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
"""

num = 0
somador = 0
contador = 0
while num != 999:
    num = int(input('Digite um número (Obs.: 999 para o programa!): '))

    if num == 999:
        break
    somador += num
    contador += 1
print(f'A Soma entre os {contador} valores digitados foi {somador}')