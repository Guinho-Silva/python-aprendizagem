primeiro = int(input('Primeiro Termo: '))

razao = int(input('Razão: '))

termo = primeiro
contador = 1

while contador <= 10:
    print(termo)
    termo += razao
    contador += 1
    