# Excecption is an event/error that interrupts the flow of the program like ZeroDivisionError, TypeError (like operation on a wrong datatype), ValueError (invaild type conversion str->int )

#1. try (executing a code snippet)
#2. except (catching the error)
#3. finally (crucial for clean ups like closing a open file after work is done)

try:
    number = int(input("Enter a number only (not zero) = "))
    print(1/number)
    
except ZeroDivisionError:#if zero is inputted
    print("Told you to not input zero.")

except ValueError:#if a string or char is inputted
    print("Only Integers except zero please.")

except Exception:
    print("This catches any exception like an else statement, so put this at last")

#finally executes even after a exeception
finally:
    print("This need some clean up.")