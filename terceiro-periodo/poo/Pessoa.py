class Pessoa:
    def __init__(self, nome, cpf, altura, idade, profissao, salario):
        self.nome = nome
        self.__cpf = cpf
        self.altura = altura
        self.idade = idade
        self.profissao = profissao
        self.__salario = salario
    
    def mostrar_cpf(self):
        return self.__cpf

    def mostrar_salario(self):
        return self.__salario

pessoa1 = Pessoa("Andrey", "065.879.947-92", 1.54, 19, "Representante Comercial", 1500)

cpf = pessoa1.mostrar_cpf()

print(f"{cpf[:3]}********{cpf[12:]}")

# print(
#     f"""
# Nome: {pessoa1.nome}
# CPF: {pessoa1.mostrar_cpf()}
# Altura: {pessoa1.altura}
# Idade: {pessoa1.idade}
# Profissão: {pessoa1.profissao}
# Salario: {pessoa1.mostrar_salario()}
# """
# )