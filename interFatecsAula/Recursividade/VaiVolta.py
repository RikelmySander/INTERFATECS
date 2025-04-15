def vaivolta(n):
    if n == 0: return
    else:
        print(n)
        vaivolta(n-1)
        print(n)

vaivolta(3)