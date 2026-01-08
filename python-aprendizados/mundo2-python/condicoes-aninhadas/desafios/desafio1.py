ValorCasa = float(input('Qual é o valor da casa?: '))

SalarioComprador = float(input('Qual é o seu salário?: '))

QtdAnos = int(input('Em quantos anos pretende pagar?: '))

QtdMeses = QtdAnos * 12

PrestacaoMaxima = SalarioComprador * 0.30
prestacaoMensal = ValorCasa / QtdMeses

if PrestacaoMaxima >= prestacaoMensal:
    print('Aprovado')
    print('Prestação mensal: {:.2f}'.format(prestacaoMensal))
else:
    print('negado')
    print('Prestação mensal: {:2f}'.format(prestacaoMensal))

'''
Escreva um programa para aprovvar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da CASA, o SÁLARIO do comprador e em QUANTOS ANOS ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo é negado.
'''