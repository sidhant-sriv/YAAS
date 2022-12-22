import math
n = eval(input())
prime = palindrome= False
def check_palindrome(s):
    return s==s[::-1]
def prime_check(t):
    if t==1:
        return False
    for i in range(1,math.sqrt(t)):
        if t%i==0:
            return False
    return True
for i in n:
    if type(i) is str:
        if check_palindrome(i):
            palindrome = True
    elif type(i) is int:
        if prime_check(i):
            prime = True
for i in n:
    if type(i) is complex and prime:
        i = complex(i.imaginary, i.real)
    elif type(i) is str and prime:
        i = i[::-1]
for i in n:
    if type(i) is complex and palindrome:
        i = i.conjugate()
    elif type(i) is int and palindrome:
        i = -i
if (prime and palindrome) == True:
    print(n[len(n)//2])
if (prime or palindrome)== False:
    res = []
    for i in n:
        if type(i) is str:
            i = list(i)
            res.append(i)
        else:
            res.append(i)
    print(res)
#Untested code


        
