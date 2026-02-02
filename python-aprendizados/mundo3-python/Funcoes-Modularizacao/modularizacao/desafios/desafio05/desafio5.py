
from utilizadesCeV import moeda

def resumo(p, desc, aume):
    print(f'O preço passado foi: {moeda.moeda(p)}')
    print(f'Com um desconto de {desc}%: {moeda.diminuir(p, True)} ')
    print(f'Com um aumento de {aume}%: {moeda.aumentar(p, True)}')
    print(f'O dobro de {moeda.moeda(p)} é de: {moeda.dobro(p, True)}')
    print(f'A metade de {moeda.moeda(p)} é de: {moeda.metade(p)}')



resumo(500, 13, 10)
