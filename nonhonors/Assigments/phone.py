phone_num = int(input("Please enter your phone number: "))

acode = phone_num//10000000
prefix = acode % 1000
line_number = phone_num % 10000

print(f"Phone number: ({acode}) {prefix}-{line_number}")