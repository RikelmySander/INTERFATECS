def mentirinha(n):
    qtd_divisores = 0
    for pd in range(1, n + 1):
        if n % pd == 0:
            qtd_divisores += 1
    if qtd_divisores == 3:
        return True
    else:
        return False
def main():
    n = int(input())

    print('sim' if mentirinha(n) else 'nao')
main()