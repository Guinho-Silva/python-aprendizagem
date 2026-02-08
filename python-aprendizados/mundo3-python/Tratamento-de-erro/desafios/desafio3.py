'''
3)Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples

O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas'''



def leiaint(msg):

    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print('Digite uma opção válida!')

def leiaidade(msg):
    while True:
        try:
            idade = int(input(msg))
            return idade
        except:
            print('Digite um número valido')

def linhas(tamanho = 42):
    return '-' * tamanho

def menu(msg):
    print(linhas())
    print(msg.center(42))
    print(linhas())

def opcoes(lista):
    menu('MENU PRINCIPAL')
    cont = 1
    for valores in lista:
        print(f'{cont}- {valores}')
        cont +=1
    opcao = leiaint('Digite sua opção: ')
    return opcao


def cadastrar():
    listaCad = list() 
    
    while True:

        opcao = opcoes(['opc1', 'opc2', 'opc3'])

        if opcao == 1:
            print(linhas())
            print(menu('PESSOAS CADASTRADAS'))
            print(linhas())
            if not listaCad:
                print('Nenhumma pessoa cadastrada.')
        
        elif opcao == 2:

            nome = str(input('Nome: '))

            idade = leiaidade('Idade: ')

            listaCad.append([nome, idade])
            print('Cadastrado(a) com sucesso!')
            
        elif opcao == 3:
            print('Saindo...')
            break

        else:
            print('Opção inválida')
    return listaCad

    

cadastro = cadastrar()
print(cadastro)



