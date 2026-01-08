'''5) Crie um programa que tenha uma tupla única com nomes de produtos  seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular'''


LojasProduto= (
    'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.20, 'Livro', 34.90
)

for produtos in range(0, len(LojasProduto)):
    if produtos % 2 ==0:
        print(f'{LojasProduto[produtos]:.<30}', end=' ')
    else:
        print(f'R${LojasProduto[produtos]:.2f}')