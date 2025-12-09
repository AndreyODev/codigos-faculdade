class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f""" 
Meu nome é {self.nome} e tenho {self.idade} anos 
"""
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def __str__(self):
        return super().__str__() + f" e leciono em {self.disciplina}"
    
p = Professor("Andrey", 19, "Fisica")

print(p)