Media1 = float(input('Digite sua 1° nota: '))

Media2 = float(input('Digite sua 2° nota: '))

TotMedia = (Media1 + Media2) / 2

if TotMedia < 5:
    print('REPROVADO!')
elif TotMedia >= 5 and TotMedia < 7:
    print('RECUPERÇÃO!')
else:
    print('APROVADO!')


'''
Crie um program que cleia as notas de um aluno e calcule sua média, mostrando no final de acordo com média atingida:

- Méida abaixo de 5:
REPROVADO

- Média entre 5 e 6.9:
RECUPERAÇÃO

-Méida 7.0 ou superior:
APROVADO
'''