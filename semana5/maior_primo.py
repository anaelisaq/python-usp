def eh_primo(k):
    if k < 2:
        return False
    i = 2
    while (i * i) <= k:
        if k % i == 0:
            return False
        i += 1
    return True

def maior_primo(n):
    numero = n
    while numero >= 2:
        if eh_primo(numero):
            return numero
        numero -= 1

print(maior_primo(100))
print(maior_primo(7))
