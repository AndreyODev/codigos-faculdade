# 6. Crie uma função que lê o ano de nascimento de uma pessoa 
# e o ano atual. 
# Calcule e mostre qual é: a idade da pessoa em anos, 
# a idade da pessoa em meses, a idade da pessoa em dias 
# e a idade da pessoa em semanas.

def calcular_idade_completa(ano_nascimento: int, ano_atual: int):
  
    idade_anos = ano_atual - ano_nascimento

    idade_meses = idade_anos * 12
    idade_dias = idade_anos * 365
    idade_semanas = idade_dias / 7

    print(f'''
    Cálculo da Idade:
    --------------------------
    Ano de Nascimento: {ano_nascimento}
    Ano Atual: {ano_atual}
    --------------------------
    Idade em Anos: {idade_anos}
    Idade em Meses: {idade_meses}
    Idade em Dias (aproximado): {idade_dias}
    Idade em Semanas (aproximado): {idade_semanas:.2f}
    ''')

calcular_idade_completa(2005, 2024)

def calcular_idade_anos(ano_nasc: int, ano_atual: int) -> int:

    return ano_atual - ano_nasc

def calcular_idade_meses(idade_anos: int) -> int:
    return idade_anos * 12

def calcular_idade_dias(idade_anos: int) -> int:
    return idade_anos * 365

def calcular_idade_semanas(idade_dias: int) -> float:
    return idade_dias / 7

# Chamada das funções
anos = calcular_idade_anos(2005, 2024)
meses = calcular_idade_meses(anos) 
dias = calcular_idade_dias(anos)  
semanas = calcular_idade_semanas(dias) 

print(f'''
    Anos: {anos}
    Meses: {meses}
    Dias: {dias}
    Semanas: {semanas:.1f}
    ''')