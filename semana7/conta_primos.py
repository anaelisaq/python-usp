def é_primo(numero):
    if numero < 2:
        return False
    i = 2
    while i <= numero**0.5:
        if numero % i == 0:
            return False
        i += 1
    return True


def n_primos(n):
    quantidade = 0
    numero = 2
    while numero <= n:
        if é_primo(numero):
            quantidade += 1
        numero += 1
    return quantidade


n = int(input("Digite um número inteiro maior ou igual a 2: "))
resultado = n_primos(n)
print("A quantidade de números primos entre 2 e", n, "é:", resultado)
