class termom:
    def __init__ (self, temp):
        self.temp = temp
        if temp < 36:
            return "Hipotemia"
        elif temp >= 36 and temp <= 36.5:
            return "Normal"
        elif temp > 36.5 and temp <= 37.5:
            return "Pré febre"
        else:
            return "Febre"

result = termom(36)
print(result)


