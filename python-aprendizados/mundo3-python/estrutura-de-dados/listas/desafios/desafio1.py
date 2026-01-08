'''1)Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior valor digitado e o menor valor digitado e as suas respectivas posições na lista
'''

valoresNum = []


for valores in range(0,5):
    valoresNum.append(int(input('Digite um valor: ')))

print(f'Os valores digitados foram: {valoresNum}')

print(f'O maior valor digitado foi: {max(valoresNum)}')

print(f'O menor valor digitado foi: {min(valoresNum)}')