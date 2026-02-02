def aumentar(num, Show=False):

    while True:
        valor = num * (1 + 10/100)
        break
    return moeda(valor) if Show else valor

def diminuir(num, Show=False):

    while True:
        reajuste = num * (1 - 13/100)
        break
    return moeda(reajuste) if Show else reajuste

def dobro(num, Show=False):

    while True:
        dobro = num * 2
        break
    return moeda(dobro) if Show else dobro

def metade(num, Show=False):
    while True:
        
        metade = num / 2
        break
    return moeda(metade) if Show else metade

def moeda(num):
     
    return f"R$ {num:.2f}".replace('.', ',')

def resumo(p, desc, aum):
    print(f'O preço digitado foi: {p}')
    print(f'Com {desc}% de desconto: {moeda.diminuir(p)} ')
    print(f'Com {aum}% de aumento: {moeda.aumentar(p)}')
    print(f'O dobro de {p} é de: {moeda.dobro(p)}')
    print(f'A metade de {p} é de: {moeda.metade(p)}')