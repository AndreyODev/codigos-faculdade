import random
import string
def gerar_tamanho(tamanho):
    if tamanho == 0:
        return ""
    return gerar_tamanho(tamanho -1) + random.choice(string.ascii_letters + string.digits) 
senha = gerar_tamanho(6)

def criptografia(tamanho, p, i=0):
    if i == len(tamanho):
        return ""
    cripto = chr(ord(tamanho[i]) +p)
    return cripto + criptografia(tamanho, p, i+1)
result = criptografia(senha, 3)
print(f"Senha gerada: {senha}")
print(f"Senha criptografada: {result}")









