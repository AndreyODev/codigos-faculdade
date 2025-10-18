def cont_digitos(n):
    if n < 10:
        return 1
    return 1 + cont_digitos(n//10)
resultado = cont_digitos(234)
print(resultado)