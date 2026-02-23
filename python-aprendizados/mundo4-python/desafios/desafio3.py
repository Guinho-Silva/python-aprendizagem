"""3) Crie uma classe chamada churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa

Considere:
-Consumo padrão: 400g por pessoa
-Preço: R$82,40/kg
"""

class churrasco:
    def __init__(self, qtde):

        self.QtdePessoas = qtde

        self.QtdeCarne = self.QtdePessoas * 0.4

        self.CustoTot = self.QtdeCarne * 82.40
    
        self.PrecoPessoa = self.CustoTot / self.QtdePessoas

    def mensagem(self):
    
     return f"Quantidade de pessoas: {self.QtdePessoas}\nQuantidade de carne a ser comprada em (Kg): {self.QtdeCarne}Kg\nCusto total do churrasco em (R$): {self.CustoTot:.2f}R$\nPreço por pessoa a ser pago (R$): {self.PrecoPessoa:.2f}R$"
    

teste = churrasco(15)


print(teste.mensagem())
