def is_hardy_ramanujan(n):
    res = 0
    for i in range(1, n):
        for j in range(i, n):
            if i**3 + j**3 == n:
                res += 1
    return res==2
print(is_hardy_ramanujan(1729))