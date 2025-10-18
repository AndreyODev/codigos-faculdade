def fibon(posicao):
    if posicao == 1:
        return 0
    elif posicao == 2:
        return 1
    return fibon(posicao -1) + fibon(posicao -2)
result = fibon(5)
print(result)
#0 1 1 2 3 5 8 13