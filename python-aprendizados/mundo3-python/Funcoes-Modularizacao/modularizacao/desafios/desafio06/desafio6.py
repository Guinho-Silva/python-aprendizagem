'''6) Dentro do pacote utilidadesCeV que criamos no desafio 5, temos um modulo chamado dado. Crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários'''

from utilizadesCeV import dado, moeda

valor = dado.leiaMoney('Digite um valor: ')


print(f'O preço passado foi:{moeda.moeda(valor)}')
print(f'Desconto de 13%: {moeda.diminuir(valor, True)}')
print(f'Aumento de 10%: {moeda.aumentar(valor, True)}')
print(f'Dobro: {moeda.dobro(valor, True)}')
print(f'Metade: {moeda.metade(valor, True)}')