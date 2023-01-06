def f_to_c(temp):
  return ((temp-32)*5)/9
def c_to_f(temp):
  return ((c*9)/5)+32
ch=eval(input("\t\t1.centigrade to fahrenheit\n\t\t2.Fahrenheit to Centigrade\t\t\n:"  ))
temp = eval(input("\nTempareture="))
print("Temp. in C=", f_to_c(temp)) if ch==1 else (print("Temp. in F=", c_to_f(temp))if ch ==2 else 0)
