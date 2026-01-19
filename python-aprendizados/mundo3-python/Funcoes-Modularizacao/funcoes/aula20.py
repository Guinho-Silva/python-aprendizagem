# Aula 20 Funções
'''
a = 5

b = 4

s = a + b

print(s)

a = 8

b = 9

s = a + b

print(s)

a = 2

b = 1

s = a + b

print(s)
'''
# Usando Função
'''
def soma (a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)
'''
#Teste 2
'''
def soma (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')



soma(10, 15)
'''

#Desempacotamento
'''
def contador(*num):
    for valor in num:
        tam = len(num)
        print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
'''
# Usando listas
'''
def dobra(lst):
    pos = 0
    
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores=[7,2,5,0,4]
dobra(valores)
print(valores)
'''
#Desempacotamento

def soma(* valores):
    s = 0

    for num in valores:
        s +=num
    print(f'Somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4)

