'''
2) Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os e uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
'''

ValoresTot = []

Valores_Pares = []

Valores_Impares = []

for valores in range(0, 7):
    valores = int(input('Digite um valor: '))

    if valores % 2 == 0:
        Valores_Pares.append(valores)
    else:
        Valores_Impares.append(valores)

Valores_Pares.sort()
Valores_Impares.sort()


ValoresTot.append(Valores_Pares[:])
ValoresTot.append(Valores_Impares[:])

print(f'Os valores pares foram: {ValoresTot[0]}')
print(f'Os valores ímpares foram: {ValoresTot[1]}')



