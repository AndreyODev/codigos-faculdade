def cont_digitos(n):
    c = 0 
    while n > 0: 
        n //= 10
        c += 1
    return c
resultado = cont_digitos(2345)
print(resultado)