def main():
  ps = input("Please enter your password: ")
  s =  ps.replace('o','0').replace('i','1').replace('a','@').replace('e','3').replace('A','4').replace('B','8').replace('s','$')
  print("Your new strong password is: ", s+'!')
  print(len(ps))
  print(ps[0])
main()
