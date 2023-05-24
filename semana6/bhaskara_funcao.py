import math

def main(a, b, c):
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

def delta(a, b, c):
    return b ** 2 - (4 * a *c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("esta equação não possui raízes reais.")
    elif d == 0:
        raiz = (-b + math.sqrt(d)) / (2 * a)
        print("a raiz dupla desta equação é", raiz)
    else:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        raiz2 = (-b - math.sqrt(d)) / (2 * a)
        if raiz1 < raiz2:
            print("as raízes da equação são", raiz1, "e", raiz2)
        else:
            print("as raízes da equação são", raiz2, "e", raiz1)