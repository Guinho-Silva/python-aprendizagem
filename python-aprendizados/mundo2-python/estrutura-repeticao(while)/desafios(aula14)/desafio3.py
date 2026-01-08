n1 = float(input('Digite o valor do 1°valor: '))

n2 = float(input('Digite o valor do 2°valor: '))


opcao = 0

while opcao != 5:
    print('''
        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos números
        [5]Sair do programa
    ''')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre os dois números é de {}'.format(soma))
    elif opcao == 2:
        multi = n1 * n2
        print('O produto entre os dois números é de {}'.format(soma))
    elif opcao == 3:
        if n1 > n2:
            print('O maior valor digitado foi {}'.format(n1))
        else:
            print('O maior valor digitado foi {}'.format (n2))
    elif opcao == 4:
        n1 = float(input('Digite o valor do 1°valor: '))

        n2 = float(input('Digite o valor do 2°valor: '))
    else:
        print('Opção inválida. Tente novamente!')
print('Você saiu do programa!')