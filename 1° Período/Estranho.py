N = int(input("Informe um número: "))
if N % 2 != 0:
    print ("Estranho")
elif N % 2 == 0 and N >=2 and N <=5:
    print ("Não estranho")
elif  N % 2 == 0 and N >=6 and N <=20:
    print ("Estranho")
else:
    print ("Não estranho")

