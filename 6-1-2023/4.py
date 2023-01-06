print("Enter your choice\t1. KM to M \n\t\t\t 2.M to KM")
ch=eval(input())
print("KM-M=", eval(input())*1000) if ch==1 else(print("KM-M=", eval(input())*0.001) if ch == 2 else 0)