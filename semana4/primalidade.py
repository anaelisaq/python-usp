n = int(input("Digite um número inteiro: "))

i = 2

while i < n:
    if n % i == 0:
        print("não primo")
        break
    i += 1
else:
    print("primo")