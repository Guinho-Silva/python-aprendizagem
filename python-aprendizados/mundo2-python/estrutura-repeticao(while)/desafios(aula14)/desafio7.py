n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t1
    t2 = t3
    cont += 1
print('FIM')