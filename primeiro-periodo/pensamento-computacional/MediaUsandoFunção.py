#No primeiro período fiz assim:
#def calcule():
    #p1 = float(input('Informe a nota da p1: '))
    #p2 = float(input('Informe a nota da p2: '))
    #return (p1 + p2)/2

#media = calcule()
#print(media)

#Agora faço assim, pq não é um bom hábito usar input dentro da função
def calcule(p1, p2):
    return (p1 + p2)/2

p1 = float(input('Informe a nota da p1: '))
p2 = float(input('Informe a nota da p2: '))

media = calcule(p1, p2)
print(media)

