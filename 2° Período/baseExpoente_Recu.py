def potencia(b, exp):
    if exp == 0:
        return 1
    return b * potencia(b, exp-1)
resultado = potencia(5, 2)
print(resultado)