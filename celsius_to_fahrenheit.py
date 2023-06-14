#!/usr/bin/env python3
#C:\Users\Helen Reumann\qis101\labs\MyTasks\celsius_to_fahrenheit.py
"""celsius_to_fahrenheit.py"""

# This program allows the user to convert a range (specified by the user) of 
# Celsius values to Fahrenheit

def main() -> None:
    
    # Specify the range of celsius values you want to convert
    
    lowerCVal = -44 # lower range
    upperCVal = 106 # upper range
    stepVal = 4 # step value


    # The for loop will calculate and print the equivalent Fahrenheit values of
    # the Celsius values in the range of values previously specified by the user
    for celsius in range(lowerCVal, upperCVal, stepVal):  
        
        # Convert from Celsius to Fahrenheit 
        fahrenheit: float = (celsius * (9/5)) + 32



        # The scope of the if statement will execute once the last celsius value within
        # the given range has been reached 

        # (upperCVal-celsius)%stepVal) = the difference between the upper range value 
        # and the last value within the range 

        if (((upperCVal-celsius)%stepVal) + celsius) == upperCVal:

            # This will print the last value within the range
            print(f"{celsius:>6.2f} °C = {fahrenheit:>6.2f} °F")

            # This will include the conversion of the upper range Celsius value
            fahrenheit = (upperCVal * (9/5)) + 32
            print(f"{upperCVal:>6.2f} °C = {fahrenheit:>6.2f} °F")

        # The scope of the else statement will execute as long as the last 
        # Celsius value in the range has not been reached
        else:
    
            # Print the Fahrenheit equivalent of each Celsius value to the hundredth 
            print(f"{celsius:>6.2f} °C = {fahrenheit:>6.2f} °F")

        
if __name__ == "__main__":
    main()




