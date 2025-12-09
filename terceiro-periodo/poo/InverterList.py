lista = [1, 2, 3, 4, 5]

def inverter(lista):
    fatiar = lista[::1]
    return fatiar

result = inverter(lista)
print(result)