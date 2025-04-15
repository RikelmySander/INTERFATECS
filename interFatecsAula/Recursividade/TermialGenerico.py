def termial(n):
    if n == 0: return 0
    else:
        return n + termial(n-1)

print(termial(4))