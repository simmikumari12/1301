
month = str(input("Please enter the month: ")).lower()
day = int(input("Please enter the day: "))
months =["january", "february", "march", "april", "may", "june", "july","august", "september", "october","november","december"]
days = []

def months():
    if month in months[2:6]:
        return "Autumn"  
    elif month in months[5:9]:
        return "Winter"
    elif month in months[9:13]:
        return "Spring"
    else:
        return "Summer"
    
def days():
    pass


def main():
    print(f"{month} {day} is summer in the southern hemisphere")
     
