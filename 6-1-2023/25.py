def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
def is_special(num):
    
    digit_sum = [int(digit) for digit in str(num)]
    digit_sum = list(map(factorial, digit_sum ))
    return sum(digit_sum) == num
print(is_special())