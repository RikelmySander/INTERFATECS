def cp(n):
    if n == 0:
        return
    cp(n-1)
    print(n)
cp(3)