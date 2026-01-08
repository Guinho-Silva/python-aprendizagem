"""2) Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
"""

while True:
    tabuada = int(input('Digite um valor para mostrar a tabela de sua multiplixação: '))
    
    if tabuada < 0:
        break

    valorTot = 1 

    while valorTot != 10:
        valorTot += 1
        multiplica = tabuada * valorTot
        print(f'{tabuada} x {valorTot} = {multiplica}')
 
print('O programa foi interrompido!')

    