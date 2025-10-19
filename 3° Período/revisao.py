class Loja:
    def __init__(self):
        self.catalogo = []  #Lista para guardar os produtos

    def realizar_venda(self):
        pass  #Vai ser implementado depois

    def oferecer_promocao(self):
        pass  #Vai ser implementado depois

    def adicionar_produto(self, produto, valor):
        self.catalogo.append({"produto": produto, "valor": valor})  #Adicionando o produto ao catálogo

    def remover_produto(self, produto):
        for p in self.catalogo:
            if p["produto"] == produto:
                self.catalogo.remove(p)  #Removendo o produto

    def listar_produtos(self):
        for p in self.catalogo:
            print(f"Produto: {p['produto']} - Valor: {p['valor']}")  #Mostrando os produtos


class Conta:
    def __init__(self, nome_cliente, numero_conta, agencia, saldo, limite_cheque_especial, limite_cartao, pix, senha):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = saldo
        self.limite_cheque_especial = limite_cheque_especial
        self.limite_cartao = limite_cartao
        self._pix = pix
        self.__senha = senha  #Senha privada

    def cadastrar(self):
        print(f"Conta de {self.nome_cliente} cadastrada com sucesso.")

    def autenticar(self, senha):
        return self.__senha == senha  #Verificando se a senha está correta

    def cadastrar_pix(self, chave_pix):
        self._pix = chave_pix  #Definindo a chave Pix

    def pix(self, chave_pix_origem, valor, conta_destino):
        #Fazendo uma transferência via Pix
        if self._pix == chave_pix_origem and self.saldo >= valor:
            self.saldo -= valor
            conta_destino.depositar(valor)
            return True
        return False

    def cheque_especial(self, valor):
        #Usando o limite do cheque especial
        if valor <= self.limite_cheque_especial:
            self.saldo += valor
            return True
        return False

    def cartao_credito(self, valor):
        #Usando o cartão de crédito
        if valor <= self.limite_cartao:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        self.saldo += valor  #Adicionando valor à conta

    def debito(self, valor):
        #Verificando se tem saldo suficiente
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False


class LojaFisica(Loja):
    def __init__(self):
        super().__init__()
        self._desconto = None  

    def realizar_venda(self, metodo, conta, item_index):
        #Verificando se o índice do item é válido
        if item_index < 0 or item_index >= len(self.catalogo):
            print("Produto não encontrado.")
            return

        item = self.catalogo[item_index]
        valor = item['valor']
        produto = item['produto']

        #Aplicando o desconto
        if self._desconto:
            valor *= (1 - self._desconto)

        sucesso = False

        #Escolhendo o método de pagamento
        if metodo == "debito":
            sucesso = conta.debito(valor)
        elif metodo == "credito":
            sucesso = conta.cartao_credito(valor)
        elif metodo == "cheque":
            sucesso = conta.cheque_especial(valor)
        else:
            print("Método inválido.")
            return

        if sucesso:
            print(f"Venda de {produto} realizada com sucesso por R${valor:.2f}.")
        else:
            print("Não foi possível concluir a venda.")

    def oferecer_promocao(self, desconto):
        self._desconto = desconto  #Define o valor do desconto
        print(f"Desconto de {desconto*100:.0f}% aplicado.")

#Criando a conta 
conta1 = Conta("Andrey", 1234, 321, 1000, 500, 1200, "andrey@pix", "1qaz2wsx")
conta1.cadastrar()  #Cadastrando a conta

#Criando a loja
loja = LojaFisica()

#Adicionando produtos na loja
loja.adicionar_produto("Mouse", 20)
loja.adicionar_produto("Teclado", 50)

#Removendo um produto
loja.remover_produto("Mouse")

#Listando produtos da loja
loja.listar_produtos()

#Aplicando uma promoção de 10%
loja.oferecer_promocao(0.10)

#Realizando uma venda com cartão de crédito
loja.realizar_venda("credito", conta1, 0)