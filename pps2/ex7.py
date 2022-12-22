n = list(map(str, input().split(" ")))
l = int(input())
s = int(input())
d = {}
for i in range(len(n)):
    d[n[i]] = i + 1
print(d)
import itertools


def combinations(n, s):
    comb = itertools.combinations(n, s)
    return ["".join(c) for c in comb]


def get_score(n):  # Return score of the word
    res = 0
    for i in n:
        res += d[i]
    return res


t = []
z = sorted(combinations(n, s))
for i in z:
    t.append(get_score(i))
for i in range(len(t)):
    if t[i] == l:
        print(z[i])
