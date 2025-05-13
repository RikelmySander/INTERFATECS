def quanto_vale(dm):
    soma = 0
    for caractere in dm:
        if caractere == '*':
            soma += 0
        elif caractere == '.':
            soma += 1
        elif caractere == '-':
            soma += 5
    return soma

def converte(nm):
    nm = list(reversed(nm))
    expoente = 0
    soma = 0
    for dm in nm:
        soma += quanto_vale(dm) * 20 ** expoente
        expoente += 1
    return soma

def main():
    nm = input()
    while nm != '*':
        nm = nm.split()
        print(converte(nm))
        nm = input()
    print(0)
main()