import random
import math

try:
    radius = int(input("Please enter the radius of hemisphere "))
    volume = (4 * math.pi * pow(radius,3))/3
    print(f"The volume of sphere with radius of {radius} is {volume:0.2f} ")
except ValueError:
    print("Invalid Input")

num = random.randint(1,11)
print(f"The factorial of {num} is {math.factorial(num)}")
    
