lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

'print(lanche)'

'print(lanche[1])'

'print(lanche[1:3])'

'print(lanche[2:])'

'print(lanche[:2])'

'print(lanche[-2])'

'print(lanche[-2:])'

'print(lanche[-3:])'

'''for comida in lanche:
    print(f'Eu vou comer{comida}')'''

'print(len(lanche))'

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Eu comi pra caramba!')'''

'print(sorted(lanche))'

#novos testes de tuplas

'''a =(2, 5, 4)

b = (5, 8, 1, 2)

c = a + b'''

'print(a)'
'print(b)'
'print(c)'
'print(len(c)) '#mostra o valor inteiro da tupla, neste caso c vale as duas tuplas anterior

'print(c.count(5))' #mostra quantas vezes um elemento aparece dentro da tupla

'print(c.index(8))'#ele mostra em que posição um determinado elemento se encontra

# mais exemplo

pessoa = ('Iago', 20, 'M', 75.25)

print(pessoa)