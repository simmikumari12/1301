import math
grades = [83, 85, 72, 65, 76, 90, 79, 88,93,70,67,80]

day1 = ['Mary', 'Jake', 'Sam', 'Alex', 'Percy', 'Jessica', 'Trent', 'Mahmoud']
day2 = ['Jake', 'Sam', 'Alex', 'Percy','Mahmoud', 'Trent', 'Caleb', 'Zayne']

print(f"{len(grades)} students took the exam.")
print(f"The highest grade was a {max(grades)}")
print(f"The lowest grade was a {min(grades)}")
print(f"The average grade for the exam was a {sum(grades)/len(grades):0.1f}", end = '\n \n')



