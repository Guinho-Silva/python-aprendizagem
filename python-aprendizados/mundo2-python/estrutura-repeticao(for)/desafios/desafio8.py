from datetime import date

AnoAtual = date.today().year

menores = []

maiores = []

for c in range(1, 7 + 1):
    AnoNascimento = int(input('Digite o ANO de nascimento: '))
    Conversao = AnoAtual - AnoNascimento

    if Conversao < 21:
        menores.append(Conversao)
        
    else:
        maiores.append(Conversao)
        
print('Lista de pessoas que possuem menoridade: ',menores)
print('Lista de idades que possuem maioridade: ',maiores)

'''Ou podemos fazer a variavel receber uma valor a cada condição em que ela seja ou não verdadeira:

totamaior = 0
totmenor = 0

e no laço faça com que essas duas variaveis recebam mais 1 +=

'''
