'''
5) Faça um programa que tenha uma lista chamada números e duas funções chamadas "sorteio()" e "somaPar()". A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anteriorl
'''

from random import randint

def sorteio():
   ListaSort = []
   for valores in range(5):
       ListaSort.append(randint(1,5))
   return ListaSort

def somaPar(Lista):

    soma = 0
    
    for num in Lista:

        if num % 2 == 0:
            soma += num
    return soma

ListaNum = sorteio()
print(f'Os números sorteador foram: {ListaNum}')

ListaPar = somaPar(ListaNum)
print(f'A soma dos números pares desse sorteio é: {ListaPar}')