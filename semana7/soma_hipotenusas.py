def é_hipotenusa(numero):
    i = 1
    while i < numero:
        j = i
        while j < numero:
            hipotenusa = (i**2 + j**2) ** 0.5
            if hipotenusa == numero:
                return True
            elif hipotenusa > numero:
                break
            j += 1
        i += 1
    return False


def soma_hipotenusas(n):
    soma = 0
    numero = 1
    while numero <= n:
        if é_hipotenusa(numero):
            soma += numero
        numero += 1
    return soma


n = int(input("Digite um número inteiro positivo: "))
resultado = soma_hipotenusas(n)
print("A soma das hipotenusas até", n, "é:", resultado)