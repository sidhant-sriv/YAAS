def swap(a,b):
  temp =a
  a = b
  b=temp
  return a, b

a, b = eval(input("A=")), eval(input("B="))
a, b = swap(a, b)
print("After Swap a=", a, "b=", b, )
