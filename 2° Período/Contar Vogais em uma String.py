#12. Contar Vogais em uma String 
#Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.
#12. Contar Vogais em uma String 
#Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.
nome = input('Digite um nome: ')
vogais = 'aeiou'
nome = nome.lower()
t = 0
for vogal in vogais:
    t += nome.count(vogal) 
    
print(f'O nome {nome} tem {t} vogal')