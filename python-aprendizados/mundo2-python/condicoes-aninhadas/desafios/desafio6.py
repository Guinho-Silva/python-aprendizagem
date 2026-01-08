PesoPessoa = float(input('Digite seu peso: '))

AlturaPessoa = float(input('Digite sua altura: '))


imc = PesoPessoa / (AlturaPessoa ** 2)

if imc < 18.5:
    print('Abaixo do Peso!')
elif imc < 24.9:
    print('Peso ideal!')
elif imc < 29.9:
    print('Sobrepeso!')
elif imc < 30:
    print('Obesidade')
else:
    print('Obesidade mórbida!')