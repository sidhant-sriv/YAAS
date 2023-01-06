n = input()
s = [int(n[i])*(i+1) for i in range(len(n))]
print(sum(s) == n)
