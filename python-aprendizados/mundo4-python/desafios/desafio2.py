'''
2)Crie a classe produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto
'''

class produto:
    def __init__(self, nome, preco):
        
        #Atributos
        self.nome = nome
        self.preco = preco
    

    def etiqueta(self):
        
        msg = f'{self.nome} - R$ {self.preco}'
        tamanhoMensagem = len(msg) + 4
        print('~'*tamanhoMensagem)
        print(f'  {msg}')
        print('~'*tamanhoMensagem)



teste = produto('Cebola', 2.50)


teste.etiqueta()