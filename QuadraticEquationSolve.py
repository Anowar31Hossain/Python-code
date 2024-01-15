# The quadratic equation is : ax^2+bx+c=0
import math
import cmath
a = int(input("Enter the coefficient of x^2:"))
b = int(input("Enter the coefficient of x:"))
c = int(input("Enter the constant number:"))


discriminant = (b**2-4*a*c)

if  (discriminant >= 0):
    x1 =(-b + math.sqrt(discriminant))/(2*a)
    x2 =(-b - math.sqrt(discriminant))/(2*a)
    print(f"The first root of is x1 = {x1:.4f}")
    print(f"The second root of is x2 = {x2:.4f}")



else:
    x1 =(-b + cmath.sqrt(discriminant))/(2*a)
    x2 =(-b - cmath.sqrt(discriminant))/(2*a)
    print(f"The solution of quadratic equation is complex.")
    print(f"The first root of is x1 = {x1.real:.4f} + i {x1.imag:.4f}")
    print(f"The second root of is x2 = {x2.real:.4f} + i {x2.real:.4f}")

