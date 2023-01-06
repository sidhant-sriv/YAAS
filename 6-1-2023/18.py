import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = (b**2) - (4*a*c)

# Find two solutions
sol1 = (-b-cmath.sqrt(discriminant))/(2*a)
sol2 = (-b+cmath.sqrt(discriminant))/(2*a)

print("The solutions are {0} and {1}".format(sol1, sol2))
