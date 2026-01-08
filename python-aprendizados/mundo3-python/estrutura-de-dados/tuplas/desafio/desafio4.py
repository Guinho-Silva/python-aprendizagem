'''4) Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9

b) Em que posição foi digitado o primeiro valor 3

C) Quais foram os números pares

'''


NumDigitados = ()


for c in range(0,4):
    Num = int(input('Digite um valor: '))

    Num = (Num,)
    NumDigitados += Num

print('Acabou')
print(NumDigitados)

print(f'Quantas vez o valor 9 apareceu?: {NumDigitados.count(9)}')


if 3 in NumDigitados:
    print(f'Em que posição foi digitado o primeiro valor 3: {NumDigitados.index(3)}')
else:
     print('O valor 3 não foi digitado!')
print(f'Números pares digitados', end=' ')

for Num in NumDigitados:
    if Num  % 2 == 0:
        print(Num, end=' ')