import random

num = random.randint(1,100)
print(num)
print("I have generated random number between 1 and 100. You will have 10 attempts to guess that number")
n = 10
while n != 0:
    try:
        user_input = int(input("Guess: "))
    except ValueError:
        pass
    if user_input == num:
        print("You Correctly guessed my random number")
        break
    if user_input < num:
        n -= 1
        if n ==0:
            print("Out of Ateempts. Better luck next time!")
        else:
            print("Your guess is less than my random number. Try Again")
    elif user_input > num:
        n-=1
        if n ==0:
            print("Out of Ateempts. Better luck next time!")
        else:
            print("Your guess is greater than my random number. Try Again")

