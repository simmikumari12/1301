from Time import *

def main():
  print("Please give me a valid time.")
  h = int(input("Enter hour (1-12): "))
  m = int(input("Enter minute (0-59)  : "))
  a = input("Enter AM or PM : ")
  time = Time(h,m,a)
  print("\nThe time you entered is " + str(time))

  while True:
    menu()
    option = input("Enter your option: ").lower()
    if option == "a":
      n = int(input("Enter number of minutes to add to the date: "))
      time = time.add(n)
      print("\nThe time obtained after adding " + str(n) + " minutes is " + str(time))
    elif option == "s":
      n = int(input("Enter number of minutes to subtract from the date: "))
      time = time.sub(n)
      print("\nThe time obtained after subtracting " + str(n) + " minutes is " + str(time))
    elif option == "p":
      time = time.previous()
      print("\nNew time is " + str(time))
    elif option == "n":
      time = time.next()
      print("\nNew time is " + str(time))
    elif option == "b":
      print("Please give me another valid time.")
      h = int(input("Enter hour (1-12): "))
      m = int(input("Enter minute (0-59)  : "))
      a = input("Enter AM or PM : ")
      time2 = Time(h,m,a)
      interval = time.minutes_between(time2)
      print("\nThe interval between " + str(time) + " and " + str(time2) + \
            " is " + str(interval) + " minutes")
    elif option == "c":
      print("Please give me another valid time.")
      h = int(input("Enter hour (1-12): "))
      m = int(input("Enter minute (0-59)  : "))
      a = input("Enter AM or PM : ")
      time2 = Time(h,m,a)
      if time.before(time2):
        print("\n" + str(time) + " is before " + str(time2)) 
      elif time.after(time2):
        print("\n" + str(time) + " is after " + str(time2)) 
      else:
        print("\n" + str(time) + " is same as " + str(time2)) 
    elif option == "q":
      break
    else:
      print("Invalid Option")

def menu():
  print("\n          Welcome to Time Tester\n")
  print("(a) Add minutes to the time. ")
  print("(s) Subtract minutes from time. ")
  print("(p) Previous minute. ")
  print("(n) Next minute. ")
  print("(b) Interval between. ")
  print("(c) Compare Times to see if one is before another. ")
  print("(q) Quit. ")
  print()

main()