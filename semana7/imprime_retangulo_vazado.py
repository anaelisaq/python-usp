largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = 1
while linha <= altura:
    coluna = 1
    while coluna <= largura:
        if linha == 1 or linha == altura or coluna == 1 or coluna == largura:
            print("#", end="")
        else:
            print(" ", end="")
        coluna += 1
    print()
    linha += 1

