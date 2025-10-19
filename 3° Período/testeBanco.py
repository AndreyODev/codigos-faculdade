class Banco:
    def __init__(self, cliente, conta, agencia, banco):
        self.cliente = cliente
        self.conta = conta
        self.agencia = agencia
        self.banco = banco
        self.senha = None

    def __str__(self):
        return f"""
Cliente: {self.cliente}
Conta: {self.conta}
Agencia: {self.agencia}
Banco: {self.banco}
"""
    def definir_senha(self, new_senha):
        if self.senha == None:
            self.senha = new_senha
            print("Sua senha foi definida!")
        elif self.senha != None:
            decisao = input("Vc já possui uma senha, deseja redefinir mesmo assim? (S/N)").upper()
            if decisao == "S":
                self.senha = new_senha
        else: 
            print("Escolha errada")
