def resumo(p, desc, aum):
    import moeda
    print(f'O preço digitado foi: {p}')
    print(f'Com {desc}% de desconto: {(moeda.diminuir(p, Show= True))} ')
    print(f'Com {aum}% de aumento: {moeda.aumentar(p, True)}')
    print(f'O dobro de {p} é de: {moeda.dobro(p,True)}')
    print(f'A metade de {p} é de: {moeda.metade(p, True)}')

resumo(500,13,10)