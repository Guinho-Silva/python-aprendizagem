'''
1) Faça um programa que tenha uma função chamada "área()", que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
'''
def mensagem(msg):
    print('-'*25)
    print(msg)
    print('-'*25)

def area(base,altura):
    
    TotArea = base * altura
    print(f'A área do terreno é {TotArea} m²')

mensagem('CONTROLE DE TERRENOS')

base = float(input('Qual é largura do terreno: '))

altura = float(input('Qual é o comprimento do terreno: '))
print()
area(base,altura)