'''
1)Crie uma classe funcionário, onde podemos cadastrar nome, setor e cargo. Crie também um médoto que permita ao funcionário se apresentar
'''
from rich import print
from rich import inspect

class funcionario:

    #Atributos de classe (global)

    empresa = 'Curso em Video'

    def __init__(self, nome, setor, cargo): #Método construtor

        #Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f'Me chamo {self.nome} sou {self.cargo} no setor de {self.setor} da empresa {funcionario.empresa}'
    
teste = funcionario('Iago', 'Dados', 'Analista de Dados')

print(teste.apresentar())
