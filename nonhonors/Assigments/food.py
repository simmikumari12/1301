menu = {
        "Hot Dog": 1.50,
        "Slice of Pizza": 1.99,
        "Whole Pizza": 9.95,
        "Soft Drink": 0.59
        } 
try:
    h = int(input("Please enter the number of Hot Dogs: "))
    p = int(input("Please enter the number of Slice of Pizza: "))
    w = int(input("Please enter the number of Whole Pizza: "))
    s = int(input("Please enter the number of Soft Drink: "))
    cost = h * menu["Hot Dog"] + p * menu["Slice of Pizza"] + w * menu["Whole Pizza"] + s * menu["Soft Drink"]
    print(f"The total cost of the order is ${cost:0.2f}")
    
except ValueError:
    print("Invalid Input")
