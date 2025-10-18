
numero = int(input ("Digite um número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print ("FizzBuzz")
else:
    if numero % 3 == 0:
        print ("Fizz") 
    if numero % 5 == 0:
        print ("Buzz")
