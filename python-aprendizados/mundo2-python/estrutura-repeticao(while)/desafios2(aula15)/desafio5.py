"""5) Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

a) Qual é o total gasto na compra

b) Quantos produtos custam mais de R$1000.

c) Qual é o nome do produto mais barato"""


Total_gasto = 0

produtos_comprados = 0

Produtos_caros = 0

preco_baratos = 0

while True:
    Nome_Produto = input('Digite o nome do produto: ')

    Preco_produto = float(input('Digite o valor do produto:  '))

    Total_gasto += Preco_produto


    if  Preco_produto > 1000:
        Produtos_caros +=1
    
    if preco_baratos == 0 or Preco_produto < preco_baratos:
        preco_baratos = Preco_produto
        produto_barato = Nome_Produto
    
    
    novamente = input('Deseja cadastrar mais produtos? [S/N]:').strip().upper()

    if novamente == 'N':
        break

print(f'O total da compra foi de: {Total_gasto}')
print(f'Há um total de {Produtos_caros} produtos acima de R$1.000')
print(f'O nome do produto mais barato foi {produto_barato}')