n = int(input())
key = list("ABBAC")
score = {}
res = {}
import pprint
def check_score(key, ans):
    score = 0
    for i in range(len(ans)):
        if ans[i] == key[i]:
            score += 2
        elif ans[i] == 'X':
            score += 0

        else:
            score -= 0.25
    return score
for i in range(n):
    c = 'C'+str(i+1)
    ans = list(map(str, input().split(' ')))
    mark = check_score(key, ans)
    if mark in score:
        score[mark] += ','+c
    else:
        score[mark] = c
res = dict(sorted(score.items())[::-1])
i = 1
print("Rank Candidates Total")
for k,v in res.items():
    print(i,v,k, sep=" ")
    i += 1

