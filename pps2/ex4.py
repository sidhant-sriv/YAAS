n = [{"Ramesh":15},{"Sid":10},{"Ramesh":16}]
def conv(n):
    res = []
    for i in n:
        for k,v in i.items():
            if type(k) is str:
                res.append([k,v])
            else:
                res.append([v,k])
    return res
t = conv(n)
for _ in range(7):
    for i in range(len(t)-1):
        for j in range(i):
            if t[i][1] == t[j][1]:
                t.append([t[i][0] + t[j][0], t[i][1]**(1/3)])
                del t[i]
                del t[j]
                break
for _ in range(7):
    for i in range(len(t)):
        for j in range(i):
            if t[i][0] == t[j][0]:
                t.append([t[i][0], str(t[i][1]) + str(t[j][1])])
                del t[i]
                del t[j]
                break


x = []
for i in t:
    x.append({i[0]:int(i[1])})
print(x)


