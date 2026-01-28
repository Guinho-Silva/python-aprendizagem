'''
5)Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação (opcional)

adicione também as docstrings a função
'''

def notas(lista):
    CadastroNotas = dict()

    CadastroNotas['Notas'] = len(lista)
    CadastroNotas['MaiorNota'] = max(lista)
    CadastroNotas['MenorNota'] = min(lista)
    CadastroNotas['MédiaTurma'] = sum(lista) / len(lista)

    return CadastroNotas

listaDados = list()

qtde = 1
while True:
    n1 = int(input(f'Digite {qtde}° nota: '))
    listaDados.append(n1)
    while True:

        resposta = str(input('Quer continuar? [S/N]')).upper()

        if resposta in 'SN':
            break
        print('Resposta inválida!Digite "S" para continuar e "N" para encerrar')
    if resposta == "N":
        break
    qtde +=1


CadNotas = notas(listaDados)
print(CadNotas)