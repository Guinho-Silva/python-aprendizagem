primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
total = 0
mais = 10

while mais != 0:
    total += mais

    while total > 0:
        print(termo)
        termo += razao
        total -= 1

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Acabou')
