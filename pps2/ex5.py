n = input()
table = [
    {"A", "J", "S"},
    {"B", "K", "T"},
    {"C", "L", "U"},
    {"D", "M", "V"},
    {"E", "N", "W"},
    {"F", "O", "X"},
    {"G", "P", "Y"},
    {"H", "Q", "Z"},
    {"I", "R"},
]
destiny = 0
soul = 0
dream = 0
vowels = "AEIOU"
for i in n:
    for j in range(len(table)):
        if i in table[j]:
            destiny += j + 1
            if i in vowels:
                soul += j + 1
            else:
                dream += j + 1
            break


def digSum(n):
    s = 0
    while n > 0 or s > 9:
        if n == 0:
            n = s
            s = 0
        s += n % 10
        n //= 10
    return s


print(digSum(destiny))
print(digSum(soul))
print(digSum(dream))
