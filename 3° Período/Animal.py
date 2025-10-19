class Animal:
    # Metodo construtor
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    # Metodo de apresentacao
    def __str__(self):
        return (f"""
        Nome: {self.nome}
        Tipo do Animal: {self.tipo}
        """)

    @classmethod
    def classificarTipo(cls):
        nome = input("Informe o nome do Animal: ")
        tipos = ["Terrestre", "Marinho", "Voador"]
        print("""
        1 - Terrestre
        2 - Marinho 
        3 - Voador
        """)
        opc = int(input("Digite um número para informar o tipo do Animal: "))

        if opc == 1:
            tipo = 0

        elif opc == 2:
            tipo = 1
        
        elif opc == 3:
            tipo = 2

        return (nome, tipos[tipo])