def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

happy_numbers = []

for i in range(1, 101):
    if is_happy(i):
        happy_numbers.append(i)

print(happy_numbers)
