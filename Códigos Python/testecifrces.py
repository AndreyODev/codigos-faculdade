#Escreva um algoritmo recursivo que crie uma senha gerada de forma aleatória 
#e que seja criptografada caractere por caractere usando uma cifra de César simples.
#Aqui está um exemplo com uma criptografia simples usando a técnica de cifra de César. 
#Esse exemplo adiciona um deslocamento de 3 posições no valor ASCII de cada caractere da senha gerada.
#Senha original: A1b2C3d4.               
#Senha criptografada: D4e5F6g7

#Usando iteração
#def cifra_cesar(senha):
    #senha_cripto = ""
    #for i in senha:
        #senha_cripto += chr(ord(i)+3)
    #return senha_cripto
#result = cifra_cesar("andrey")
#print(result)


#def cifra_cesar(senha, p, i=0):
    #if i == len(senha):
        #return "" 
    #cripto = chr(ord(senha[i]) + p)
    #return cripto + cifra_cesar(senha, p, i+1)
#result = cifra_cesar("andrey", 3)
#print(f"Senha Original: andrey \nSenha criptografada: {result}")


import random
import string

def gerar_senha(tamanho):
    if tamanho == 0:
        return ""
    else:
        return gerar_senha(tamanho - 1) + random.choice(string.ascii_letters + string.digits)
senha = gerar_senha(6)

def cifra_cesar(tamanho, p, i=0):
    if i == len(tamanho):
        return "" 
    cripto = chr(ord(tamanho[i]) + p)
    return cripto + cifra_cesar(tamanho, p, i+1)
result = cifra_cesar(senha, 3)

print(f"Senha gerada: {senha}")
print(f"Senha criptografada: {result}")
