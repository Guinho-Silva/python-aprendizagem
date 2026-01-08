'''4) Refaça o desafio 009, mostrando um número que o usuário escolher, só que agora utilizando o um laço for.
'''

Tabuada = int(input('Digite um valor a ser multiplicado: '))

for c in range (1, 10 + 1):
    m = Tabuada * c
    print ('{} x {}= {}'.format(Tabuada, c, m))
print('Fim do programa!')