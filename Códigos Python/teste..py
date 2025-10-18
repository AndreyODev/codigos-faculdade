def palindromo(string, revers=""):
    if len(string) == 0:
        return revers
    return palindromo(string[:-1], revers + string[-1])
result = palindromo("texto")
print(result)

