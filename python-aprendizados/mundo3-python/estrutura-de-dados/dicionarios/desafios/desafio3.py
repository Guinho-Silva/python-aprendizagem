'''3)
Cria um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''

from datetime import date

AnoAtual = date.today().year

Dados = dict()

while True:
    Dados['Nome'] = str(input('Nome: '))

    Dados['AnoNasc'] = int(input('Ano de nascimento (xxxx): '))

    Dados['NumCarteira'] = int(input('N° de CTPS (Digite 0 caso não tenha): '))

    Dados['Idade'] = AnoAtual - Dados['AnoNasc']

    if Dados['NumCarteira'] == 0:
        break
        
    elif Dados['NumCarteira'] != 0:
        Dados['AnoContrato'] = int(input('Ano de contratação: '))

        Dados['Salário'] = float(input('Salário: '))

        Dados['TempoTrabalhado'] = AnoAtual - Dados['AnoContrato']

        Dados['TempFaltante'] = 35- Dados['TempoTrabalhado']

        Dados['IdadeAposent'] = Dados['Idade'] + Dados['TempFaltante']
        break

print(f'O nome do cidadão é: {Dados['Nome']}')
print(f'O {Dados['Nome']} tem: {Dados['Idade']} anos.')

if Dados['NumCarteira'] != 0:
    print(f'CTPS tem o valor de: {Dados['NumCarteira']}.')
    print(f'O ano de contração foi: {Dados['AnoContrato']}.')
    print(f'O valor do salário é de: {Dados['Salário']}.')
    print(f'Tempo aposentadoria: {Dados["TempFaltante"]} anos')
    '''print(Dados)'''