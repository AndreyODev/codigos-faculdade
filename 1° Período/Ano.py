ano = int (input ("Qual é o ano? "))
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (" Este é um ano bissexto.")
else:
    print ("Este não é um ano bissexto")