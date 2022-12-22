#untested
s1 = input()
s2 = input()
if s1 in s2 or s2 in s1:
    print("MISMATCH")
    exit()
import re
s1 = re.sub('AGCT', 'm', s1)
s2 = re.sub('AGCT', 'm', s2)
t1 = t2 = []
for i in range(len(s1)):
    if s1[i]=='m':
        t1.append(i)


for i in range(len(s2)):
    if s2[i]=='m':
        t2.append(i)
if t1==t2:
    print("MATCH")
else:
    print('MISMATCH')


