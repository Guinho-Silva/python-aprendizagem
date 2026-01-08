Valor_sacar = 0
cedula = 50
Totcedula = 0

Valor_sacar = int(input('Digite o valor a ser sacado: '))

while True:

    if Valor_sacar >= cedula:
        Valor_sacar -= cedula
        Totcedula += 1
    else:
        if Totcedula > 0:
            print(f'Você receberá {Totcedula} cédula(s) de R${cedula}')

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        Totcedula = 0 

        if Valor_sacar == 0:
            break

print('Fim do programa!')
