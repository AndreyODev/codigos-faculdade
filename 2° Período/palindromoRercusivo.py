def palindromo(string, reverso=""):
    if len(string) == 0:
        return reverso
    return palindromo(string[:-1], reverso + string[-1])
palavra = "ovo"
result = palindromo(palavra)
if result == palavra:
    print(f"A palavra {result} é um palindromo")
else:
    print(f"A palavra {result} não é um palindromo")
