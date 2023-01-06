n = int(input())
s = sum([int(i) for i in str(n) ])
if n%s:
    print("It is Harshad")
else:
    print("it is not")