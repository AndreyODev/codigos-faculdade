#14. Encontrar o Maior Número em uma Lista 
#Peça ao usuário para digitar uma lista de números e exiba o maior número dessa lista.
ListaN = input('Digite uma lista de numero: ').split()
for i in range(0, len(ListaN)): 
    ListaN[i] = int(ListaN[i])
    
print(ListaN)    

maior = 0
for i in ListaN:
    if i > maior:
        maior = i
print(f'O maior numero dessa lista é {maior}')

#Poderia usar esse código tbm, esse é utilizando o max, o que deixa o código mais curto
#ListaN = []
#for i in range(3): 
    #N = int(input('Informe um numero: '))
    #ListaN.append(N)
    
#print(ListaN)   
#print(f'O maior numero dessa lista é {max(maior)}')