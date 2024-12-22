try :
    x = int(input("Please enter the number of cents: "))
    quarters = x // 25
    dimes = (x % 25)//10
    nickels = ((x %25) % 10)//5
    pennies = x % 5
    print(f"Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")
except ValueError:
    print("Not a valid Input")



