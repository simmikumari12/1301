import sys
import math
def RGB_to_CMYK():
    while True:
        try:
            #takes the RGB input from user
            print(" ")
            print('RGB to CMYK converter')

            red =  int(input("Enter the Red Color Value (enter quit or q to quit): "))
            r = red/100

            green = int(input("Enter the Green Color Value: "))
            g = green/255

            blue = int(input("Enter the Blue Color Value: "))
            b = blue/255

            print(" ")

            #Does the calculation according to the given formula to convert from RGB to CMYK
            k1 = 1 - max(r,g,b)
            s  = 1 - k1 
            c = ((1-r-k1)/s) * 100
            m = ((1-g-k1)/s) * 100
            y = ((1-b-k1)/s) * 100
            k = k1 * 100

            #Output the CMYK values
            print("CMYK Values: ")
            print("Cyan: ", round(c))
            print("Magenta: ", round(m))
            print("Yellow: ", round(y))
            print("Key(Black): ", round(k))

        except ValueError:
            sys.exit()
    
        if red == 'quit' or red == 'q' or green == 'quit' or green == 'q' or blue =='quit' or blue =='q':
            sys.exit()
    
RGB_to_CMYK()