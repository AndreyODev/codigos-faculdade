def fatorialIterativo(n):
    c = 1
    for i in range(1, n+1):
        c *= i
    return c
resultado = fatorialIterativo(5)
print(resultado)