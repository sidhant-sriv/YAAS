def find_perfect_numbers(percentage):
    res = []
    for i in range(2, 400+percentage):
        divisors = [x for x in range(1, i) if i % x == 0]
        if sum(divisors) == i:
            res.append(i)
def find_ramanujan_numbers(percentage):
    res = [468, 513, 520, 539, 559, 576, 637, 686, 728, 730, 737, 756, 793, 854, 855, 945, 1001]
    for i in range(400+percentage,1001):
        if i in res:
            return i
    return False
percentage = int(input())


#This question is under construction. I got too tired to solve it so I've left it incomplete. Thank you for your cooperation.
    
