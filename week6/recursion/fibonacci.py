# 0 - 0, 1 -1, 2 - 1


def fibo_recursion(n):
    '''fibonacci using recursion'''

    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(3))