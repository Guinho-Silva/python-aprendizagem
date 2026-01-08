'''5) Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.

No final, mostre o conteúdo das três listas geradas (teste) ola'''

valoresDigitados = []

valoresPares = []

valoresImpares = []

continuar = ''

while True:
    valores = int(input('Digite um valor: '))

    valoresDigitados.append(valores)


    if  valores % 2 == 0:
        valoresPares.append(valores)
    
    else:
        valoresImpares.append(valores)

    continuar = input('Deseja continuar?[S/N]: ').upper()

    if continuar == 'N':
        break
   

print(f'Valores digitados:{valoresDigitados}')
print(f'Valores pares: {valoresPares}')
print(f'Valores ímpares: {valoresImpares}')