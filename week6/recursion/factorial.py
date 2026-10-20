def fact(n):
    if n <  0:
        print("Factorial not defined for negative number")
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))