from time import time
from math import ceil, sqrt
 
def tempo(f, *a):
    inicio = time()
    f(*a)
    return time() - inicio
 
def primo1(n):
    qtd_divisores = 0
    for pd in range(1, n+1):
        if n % pd == 0:
            qtd_divisores += 1
    if qtd_divisores == 2:
        return True
    else:
        return False
 
def primo2(n):
    qtd_divisores = 0
    for pd in range(1, n+1):
        if n % pd == 0:
            qtd_divisores += 1
    return qtd_divisores == 2
 
def primo3(n):
    qtd_divisores = 0
    for pd in range(2, n):
        if n % pd == 0:
            qtd_divisores += 1
    return qtd_divisores == 0
 
def primo4(n):
    for pd in range(2, n):
        if n % pd == 0:
            return False
    return True
 
def primo5(n):
    if n % 2 == 0: return n == 2
    for pd in range(3, n, 2):
        if n % pd == 0:
            return False
    return True
 
def primo6(n):
    if n % 2 == 0: return n == 2
    metade = n // 2
    for pd in range(3, metade+1, 2):
        if n % pd == 0:
            return False
    return True
 
def primo7(n):
    if n % 2 == 0: return n == 2
    raiz = ceil(sqrt(n))
    for pd in range(3, raiz+1, 2):
        if n % pd == 0:
            return False
    return True
