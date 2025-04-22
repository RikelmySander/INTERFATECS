from time import time

def tempo(f, *a):
    inicio = time()
    f(*a)
    return time() - inicio

def F(n):
    if n <= 2:
        return 1
    else:
        return F(n - 1) + F(n - 2)

def Fm(n, memo={}):
    if n <= 2:
        return 1
    else:
        if n not in memo:
            memo[n] = Fm(n - 1) + Fm(n - 2)
        return memo[n]

def experimento():
    for n in range(1, 41 + 1):
        t = tempo(Fm, n)
        print(f'Tempo: {t:.2f}seg')
        print('-' * 30)

