def vogal(caractere):
    caractere = caractere.lower()
    vogais = "aeiou"
    i = 0
    while i < len(vogais):
        if caractere == vogais[i]:
            return True
        i += 1
    return False

print(vogal("a"), vogal("b"), vogal("E"))