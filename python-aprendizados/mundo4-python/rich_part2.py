'''from rich import print
from rich.panel import Panel

caixa = Panel('Esse aqui é um painel de exemplo', title= 'Mensagens', style='blue', )

print(caixa)'''



# Rich 003

'''from rich import print

from rich.table import Table

table = Table(title = "Tabela de Preços")

Table.add_column("Nome")

Table.add_column("Preço")

Table.add_row('Bolacha', "3.50")

print(table)'''

#rich 004

'''from rich import print
from rich import inspect

inspect(int)'''


#rich 005

from rich.traceback import install

def division(x, y):
    return x/y

print(division(50, 0))