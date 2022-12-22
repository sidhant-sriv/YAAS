# d = list(input())
# t = ""
# for i in d:
#     if i=='’':
#         t += '"'
#     else:
#         t += i
# s = eval(''.join(d)) 
# def unpack(n):
#     res = []
#     for i in n:
#         if type(i) is list:
#             for j in unpack(i):
#                 res.append(j)
#         else:
#             res.append(i)
#     return res
# def unpack_fr(n):
#     r = unpack(n)
#     if len(r) == len(n):
#         print("cannot unpack")
#     else:
#         print(len(r))
# print(d)
n = list(input())
a = n.count('[')
if a>1: print(n.count(',')+1)
else: print("cannot unpack")

