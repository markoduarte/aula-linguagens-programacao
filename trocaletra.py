nome = input()
posicao = int(input())

if nome[posicao] == "s":
    print(nome[:posicao] + "r" + nome[posicao+1:])
elif nome[posicao] == "m":
    print(nome[:posicao] + "n" + nome[posicao+1:])
else:
    print(nome[:posicao] + nome[posicao + 1:])