'''2) Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''


continuar = ''

valoresDigitados = []

while True:
    valores = int(input('Cadastre um valor: '))

    if valores not in valoresDigitados:
        valoresDigitados.append(valores)
    else:
        print('Este valor já foi digitado!')

    continuar = input('Quer cadastrar mais números?[S/N]: ').upper()

    if continuar == 'N':
        break

valoresDigitados.sort()

print(f'Os valores digitados foram: {valoresDigitados}')