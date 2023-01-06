def find_primes(n):
    
    primes = [True] * (n + 1)

    
    primes[0] = False
    primes[1] = False

    
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False

    
    prime_list = []
    for i in range(2, n + 1):
        if primes[i]:
            prime_list.append(i)

    return prime_list


print(find_primes(20)) 
