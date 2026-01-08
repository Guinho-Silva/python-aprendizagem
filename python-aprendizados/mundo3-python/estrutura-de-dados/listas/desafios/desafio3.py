'''3) Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela'''

valoresUsuario = []

for c in range(0,5):
    valores = int(input('Digite um valor'))
    if valores == 0:
        valoresUsuario.append(valores)
    elif valores > valoresUsuario[-1]:
        valoresUsuario.append(valores)
    else:
        pos = 0
        while pos < len(valoresUsuario):
            if valores <= valoresUsuario[pos]:
                valoresUsuario.insert(pos,valores)
                break
            pos +=1
    
print(f'Os valores digitado em ordem foram{valoresUsuario}')