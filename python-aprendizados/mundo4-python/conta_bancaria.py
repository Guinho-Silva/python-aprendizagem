class ContaBancaria:

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}')
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo NEGADO de {valor:.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo -= valor

            print(f'Saque de {valor:.2f} autorizado na conta {self.id}')


Conta1 = ContaBancaria(113, "Iago", 3000)

Conta1.depositar(500)

Conta1.sacar(10000)
print(Conta1)