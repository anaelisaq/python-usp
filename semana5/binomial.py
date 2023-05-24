def fatorial (n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n, k):
    if k <= n:
        return fatorial(n) // (fatorial(k) * fatorial(n - k))
    else:
        print("K precisa ser menor ou igual a N")