# Declaração de clsses

class Gafanhoto:
    def __init__(self): # métodos construtor

        #Atributos de instancia

        self.nome = ""
        self.idade = 0

    # Métodos de Objetos
    def aniversario(self):
        self.idade = self.idade +1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

#Declaração de Objetos

g1 = Gafanhoto()

g1.nome = 'Maria'

g1.idade = 48

g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()

g2.nome = 'Adão'
g2.idade = 49

print(g2.mensagem())