'''sexo = ''

while sexo not in ('M', 'F'):
    sexo = input('Digite seu sexo [M/F]: ').upper()
    if sexo not in ('M', 'F'):
        print('Valor inválido! Digite novamente.')
print('Sexo registrado!')'''

sexo = ''

while sexo not in ('M', 'F'):
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()
    if sexo not in ('M', 'F'):
        print('Valor inválido! Digite novamente.')

print('Sexo registrado:', sexo)

