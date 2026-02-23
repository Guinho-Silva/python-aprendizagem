'''
1)Crie uma classe funcionário, onde podemos cadastrar nome, setor e cargo. Crie também um médoto que permita ao funcionário se apresentar
'''


class funcionario:
    def __init__(self, nome, setor, cargo): #Método construtor

        #Atributos
        self.nome = nome
        self.setor = setor
        self.cargo = cargo



    def apresentar(self):
        return f'Me chamo {self.nome} sou {self.cargo} no setor de {self.setor} da empresa Curso em Video'
    
teste = funcionario('Iago', 'Dados', 'Analista de Dados')

print(teste.apresentar())
