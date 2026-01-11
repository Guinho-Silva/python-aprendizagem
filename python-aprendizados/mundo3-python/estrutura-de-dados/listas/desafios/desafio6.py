'''6) Crie um programa onde o usuário digita uma expressão qualquer que usa parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta'''

Expressao = input('Digite a expressão: ')

pilha = []

for simbolo in Expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')

else:
    print('Sua expressão está inválida!')

print(pilha)
