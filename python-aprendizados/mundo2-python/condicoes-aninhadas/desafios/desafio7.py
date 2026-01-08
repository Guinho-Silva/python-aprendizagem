print('{:=^40}'.format(' LOJAS IAGO '))


PrecoProduto = float(input('Digite o valor do produto: '))


TipoPagamento = (input('Tipo de pagamento: '))

vista = ['dinheiro','cheque']



VistaCartao = PrecoProduto / 0.05


if TipoPagamento in vista:
    NovoPreco = PrecoProduto * 0.9
    print(f'Pagamento à vista (dinheiro/cheque): 10% desconto. Novo preço: R$: {NovoPreco:.2f}',NovoPreco)

elif TipoPagamento == 'cartão':
    NovoPreco = PrecoProduto * 0.95
    print(f'Pagamento com cartão à vista: 5% desconto. Novo preço: {NovoPreco:.2f}')
else:
    NovoPreco = PrecoProduto * 1.2
    print(f'Pagamento parcelado: 20% acréscimo. Novo preço: R$ {NovoPreco:.2f}')
