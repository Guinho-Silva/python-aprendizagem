# Declaração de clsses

class Gafanhoto:

    """
    Docstring para Gafanhoto

    É uma classe que cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use

    variavel = gafanhoto(nome, idade)
    """

    def __init__(self, nome='', idade = 0): # métodos construtor

        #Atributos de instancia

        self.nome = nome
        self.idade = idade

    # Métodos de Objetos
    def aniversario(self):
        self.idade = self.idade +1

   
    def __str__(self): #Double method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'
#Declaração de Objetos

g1 = Gafanhoto('Maria', 48)
g1.aniversario()
print(g1.__dict__)
#Atributo
#Retorna em dicionario
print(g1.__getstate__()) #Method

print(g1.__class__)#Retorna a classe pertecente do objeto


