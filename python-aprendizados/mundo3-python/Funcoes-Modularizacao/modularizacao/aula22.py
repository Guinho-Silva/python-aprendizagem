# Aulta teórica

''''def fatorial(n):
    fat = 1
    
    for valor in range(1, n+1):
        fat *= valor
        
    return fat

def dobro(n):
    return n * 2

def triplo(n):
    return n*3'''

import uteis

#para usar a função dentro do pacote "uteis", usasse o nome do pacote + o nome da func

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f"O fatorial de {num} é {fat}")

print(f'O dobro de {num} é {uteis.dobro(num)}')

print(f'O triplo de {num} é {uteis.triplo(num)}')