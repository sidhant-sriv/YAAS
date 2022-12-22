import string
p = tuple(input().split(','))
score = 0
special = "*&^%$#@!"
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
def check(s):
    l = c = u = k = n = 0
    for i in s:
        if i in lower:
            l = 1
        if i in upper:
            u = 1
        if i in num:
            n = 1
        if i in special:
            c = 1
    if len(s)>=6 and len(s)<=12:
        k = 1
    return sum([l,k,c,u,n])>=4
res = 0
for i in p:
    if check(i):
        print(i.strip())
    res += check(i)

if res==0:
    print("invalid")
    
    