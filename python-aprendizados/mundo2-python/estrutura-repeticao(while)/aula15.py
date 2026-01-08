'''cont = 1

while cont <= 10:
    print(cont, ' ', end='')
    cont += 1

print('Acabou!')'''

'''cont = 1 

while True:    # O programa entra em loop infinito
    print(cont, ' ', end='')
    cont += 1

print('Acabou!')'''



'''n = 0
    s = 0
    while n !=999:
        n = int(input('Digite um número: '))
        s += n
    s -= 999 # Uma gambirra muito utilizada para não considera o 999
    print('A soma vale {}'.formt(s))'''


n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #Com o comando break aqui, ele desconsidera o valor 999 e soma os demais digitados
    s += n
print(f'A soma vale {s}')



