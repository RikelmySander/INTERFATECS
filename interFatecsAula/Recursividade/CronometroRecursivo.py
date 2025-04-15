def cr(n):
    if n == 0:
        return
    print(n)
    cr(n-1)
cr(3)