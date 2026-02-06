'''
3)Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples

O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas'''

def cadastrar():
    listaCad = list() 
    
    while True:

        print('-'*30)
        print(f'{'MENU PRINCIPAL':>20}')
        print('-'*30)

        print('''
        1- Ver pessoas cadastradas
        2- Cadastrar nova pessoa
        3- Sair do Sistema
        ''')
        try:
            opcao = int(input('Digite sua opção: '))
        except:
            print('Digite uma opção valida')
            continue

        if opcao == 1:
            print('-'*30)
            print(f'{"PESSOAS CADASTRAS":>20}')
            print('-'*30)
            if not listaCad:
                print('Nenhumma pessoa cadastrada.')
        
        elif opcao == 2:

            nome = str(input('Nome: '))
            listaCad.append(nome)

            idade = int(input('Idade: '))
            listaCad.append(idade)
            print('Cadastrado(a) com sucesso!')
        elif opcao == 3:
            print('Saindo...')
            break

        else:
            print('Opção inválida')
    return listaCad

    

cadastro = cadastrar()
print(cadastro)

