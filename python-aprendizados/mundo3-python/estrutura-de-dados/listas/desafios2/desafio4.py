'''
4) Aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados

b) A soma dos valores da terceira coluna

c) O maior valor da segunda linha
'''


MatrizPrincipal = []
Soma_pares = 0
Soma_coluna = 0
MaiorValor_linha = 0
for linha in range(3):
    lista_linha = []

    for coluna in range(3):
        valores = int(input('Digite um valor: '))
    
        lista_linha.append(valores)

        if valores % 2 == 0:
            Soma_pares += valores

    MatrizPrincipal.append(lista_linha)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{MatrizPrincipal[linha][coluna]:^5}', end='')
    print()

print(f'Os valores pares são: {Soma_pares}')

for linha in range(0,3):
    Soma_coluna += MatrizPrincipal[linha][2]
print(f'A soma da dos valores da terceira coluna é: {Soma_coluna}')
print(f'O maior valor da segunda linha é: {max(MatrizPrincipal[1])}')


'''for coluna in range(0,3):
   if coluna == 0:
       MaiorValor_linha = MatrizPrincipal[1][coluna] 
   elif MatrizPrincipal[1][coluna] > MaiorValor_linha:
        MaiorValor_linha = MatrizPrincipal[1][coluna]
print(f'O maior valor da segunda linha é: {MaiorValor_linha}')'''
