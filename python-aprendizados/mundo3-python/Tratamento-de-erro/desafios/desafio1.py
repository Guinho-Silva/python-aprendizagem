'''desafio - Tratamento de Erros

1) Rescreva a função leiaint() que fizemos no modulo anterior, incluindo agora a possibilidade da digitação de um número inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.'''


def leiaint(msg):

  while True:
    try:
      
      valor = int(input(msg))
      return f'\033[32mO número digitado "{valor}" é inteiro\033[m'
    except:
      print(f'\033[31mDigite um número inteiro válido!\033[m')

def leiafloat(msg):
  while True:
    try:
      num = input(msg).replace(',','.') 
      
      if '.' not in num:
        print('\033[31mDigite um número DECIMAL (com vírgula)\033[m')
        continue     
      
      valor = float(num)

      return f'\033[32mO número digitado "{valor}" é um número decimal!\033[m'
    
    except:
      print(f'\033[31mDigite um número decimal válido!\033[m')

n1= leiaint('Digite um número inteiro: ')
print(n1)


numero = leiafloat('Digite um número real: ')
print(numero)