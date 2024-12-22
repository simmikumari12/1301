import math
a = int(input("Please enter the length of side A of the triangle (in meters): "))
b = int(input("Please enter the length of side B of the triangle (in meters): "))
c = int(input("Please enter the length of side C of the triangle (in meters): "))

s = (a+b+c)/2
print(f"The perimeter of triangle is {s*2} m")
area = math.sqrt(s * (s-a) * (s-b) * (s-c))

print(f"The area of the triangle is {area:0.2f} m^2")

if a*a + b*b == c*c:
    print("It is a Right Triangle")
elif a*a + b*b > c*c:
    print("It is a Acute Triangle")
elif a*a + b*b < c*c:
    print("It is a Obtuse Triangle")
else:
    pass

