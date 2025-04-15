def pot(x,n):
    if n == 0: return 1
    else:
        return pot(x,n-1) * x

print(pot(2,8))