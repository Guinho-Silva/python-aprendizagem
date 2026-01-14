'''
3)Crie um programa que leia uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado

No  final mostre a matriz na tela, com a formatação correta'''

matrizPrincipal = []


for linha in range(3):
    lista_linha = []

    for coluna in range(3):
        valores = int(input('Digite um valor: '))

        lista_linha.append(valores)

    matrizPrincipal.append(lista_linha)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matrizPrincipal[linha][coluna]:^5}', end='')
    print()