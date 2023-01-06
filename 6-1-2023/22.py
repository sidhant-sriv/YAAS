def is_fibonacci(n):
    
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True

    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b == n:
            return True
    return False
