# Na tupla, este comando não seria permitido, pois ela é imutável

'''
num = (2, 5, 9, 1)

num[2] = 3

print(num)
'''
# Já na lista, o número é alterado

'''
num = [2, 5, 9, 1]

num[2] = 3

print(num)
'''
#Adiciona um elemento

'''
num = [2, 5, 9, 1]

num.append(7)

print(num)
'''

#Ordernado os dados

'''
num = [2, 5, 9, 1]
num.sort()
print(num)
'''

#Desordenando

'''
num = [2, 5, 9, 1]

num.sort(reverse=True)

print(num)
'''

#Mostrando quantos elementos possui

'''
num = [2, 5, 9, 1]

print(f'Esta lista tem {len(num)} elementos')
'''

#Inserindo valores

'''
num = [2, 5, 9, 1]

num.insert(0,8)

print(num)
'''

#Removendo elementos

'''
num = [2, 5, 9, 1]

num.pop(2)

print(num)'''

#Praticando

'''valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for c, v  in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...', end='')'''


'''valores = list()

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v  in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...', end='')
print('Fim do programa!')'''

#copiando uma lista

a = [2, 3, 8, 7]

b = a[:]

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')