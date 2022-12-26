#Part A
n = int(input()) 
def take_prod():
    customer_id = input()
    product = input()
    quantity = input()
    rate = input()
    return [customer_id,product,quantity,rate]
for i in range(n):
    m = int(input())
    for i in range(m):
        x = ','.join(take_prod())+'\n'
        with open('pps2/ex14/output.csv', 'a+') as f:
            f.write(x)
#Part B Sub1
import pandas as pd
df = pd.read_csv('output.csv')
df['total'] = df.apply(lambda row: row['quantity'] * row['rate'], axis=1)
x = df.values
def f1(customer_id):
    res = 0
    for i in x:
        if i[0]==customer_id:
            res+=i[-1]
    return res
#TODO :Part B Sub2 
#TODO :Part B Sub3
print(f1(1111)) # Test for part b sub1
print(df.head())
