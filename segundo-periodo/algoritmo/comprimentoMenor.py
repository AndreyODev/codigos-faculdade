#1. Crie uma função chamada comprimentoMenor que recebe duas strings como parâmetros
#e retorna True se o comprimento da primeira string for menor do que o da segunda string,
# e False caso contrário.
def comprimentoMenor(string1, string2):
    if len(string1) < len(string2):
        return True
    return False

result = comprimentoMenor("andrey", "jeferson")
print(result)