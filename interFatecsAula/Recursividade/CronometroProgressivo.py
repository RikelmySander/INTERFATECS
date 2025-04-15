def cr(n):
    if n == 0:
        return
    cr(n-1)
    print(n)
cr(3)