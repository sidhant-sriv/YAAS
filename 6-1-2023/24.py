def is_armstrong(num):
    
    n = len(str(num))
    
    sum = 0
    
    for digit in str(num):
        
        sum += int(digit)**n
    
    return sum == num
print(is_armstrong(int(input())))