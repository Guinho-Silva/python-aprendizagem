'''6) Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais'''

tupla = ('Python', 'Curso', 'Trabalhar', 'Programador', 'Futuro', 'JavaScript', 'Estudar', 'Praticar', 'Linguagem')

print('Quaisa vogais temos nestas palavras?')

for palavras in tupla:
    print(f'\n Na palavra {palavras.upper()} temos ', end='')

    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(letra, end='')
