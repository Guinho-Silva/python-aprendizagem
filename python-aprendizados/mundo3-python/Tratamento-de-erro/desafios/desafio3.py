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

def arquivo(nome):
    try:
       arq =  open(nome, 'rt')
       arq.close()
    
    except FileNotFoundError:
        return False
    
    else:
        return True

def criaArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve algum erro na criação do arquivo!')
    else:
        print(f'O arquivo \"{nome}\" foi criado com sucesso!')

def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        menu('PESSOAS CADASTRADAS!')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            
def cadastrar(arq, nome='Não informado', idade = 0):
    try:
        arq = open(arq, 'at')
    
    except:
        print('Houve um erro ao abrir o arquivo')
    
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo cadastro de {nome} foi adicionado!')


file = 'cadastro_pessoas.txt'

if not arquivo(file):
   criaArquivo(file)

    
while True:

    opcao = opcoes(['Listar pessoas', 'Cadastrar pessoa', 'Sair'])

    if opcao == 1:
        lerArquivo(file)

        if not lerArquivo:
            print('Nenhumma pessoa cadastrada.')
    
    elif opcao == 2:
        menu('NOVO CADASTRO')
        nome = str(input('Nome: '))

        idade = leiaidade('Idade: ')

        cadastrar(file, nome, idade)
    elif opcao == 3:
        print('Saindo...')
        break

    else:
        print('Opção inválida')




