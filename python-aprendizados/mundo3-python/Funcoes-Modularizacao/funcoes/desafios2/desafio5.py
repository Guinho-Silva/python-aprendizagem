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

    """
        Programa para análise de notas de alunos.

        Este programa solicita ao usuário a digitação de várias notas, permitindo
        que ele decida quando encerrar a entrada de dados. As notas são armazenadas
        em uma lista e, ao final, são processadas por uma função chamada `notas()`.

        A função `notas()` recebe uma lista de notas e retorna um dicionário contendo:
        - A quantidade de notas informadas
        - A maior nota
        - A menor nota
        - A média da turma
    """


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

help(notas)