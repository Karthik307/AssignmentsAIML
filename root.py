import cmath
a=int(input("Enter 'a' value: "))
b=int(input("Enter 'b' value: "))
c=int(input("Enter 'c' value: "))
d=(b**2)-(4*a*c)
e =(-b-cmath.sqrt(d))/(2*a)
f=(-b+cmath.sqrt(d))/(2*a)
print(e," & ",f,"are roots.")
