
class ContaCorrente:
    def __init__(self, conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        sefl.saldo=0
        if saldo:
            self.saldo = saldo
     
    def alterarNome(self, nome):
        self.nome = nome
     
    def alterarConta(self, conta):
        self.conta = conta
     
    def alterarSaldo(self, saldo):
        self.saldo = saldo
