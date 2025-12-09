class Carro:
    def __init__(self, marca, ano, cor, placa):
        self.marca = marca
        self.ano = ano
        self.cor = cor 
        self.placa = placa
        self.is_running = True

    def __str__(self):
        return f"""
Marca: {self.marca}
Ano: {self.ano}
Cor: {self.cor}
Placa: {self.placa}
"""
    @classmethod
    def cadastro_venda(cls):
        marca = input("Marca: ")
        ano = int(input("Ano: "))
        cor = input("Cor: ")
        placa = input("Placa")
        return cls(marca, ano, cor, placa)
    
    def ligar_carro(self):
        if self.is_running == False:
            self.is_running = True
            print("O carro esta ligado ..... RUMRUMRUUM")
        else:
            print("Ja esta ligado")