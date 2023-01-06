n = int(input())
for i in range(n):
    if i*(i+1) == n:
        print("Yes")
        break
print("No")