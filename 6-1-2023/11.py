n = eval(input())
for i in range(int(n**0.5)):
    if n%i==0:
        print("Not prime")
        exit()
print("Prime")