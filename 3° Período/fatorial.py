# def fatorial(numero):
#     n = 1
#     while numero > 0:
#         n *= numero
#         numero -= 1
#     return n


# result = fatorial(6)
# print(result)

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)
    
result = fatorial(5)
print(result)