"""
Execption:
    Excecption is an event/error that interrupts the flow of the program like ZeroDivisionError, TypeError (like operation on a wrong datatype), ValueError (invaild type conversion str->int )

There are 4 parts in exception handling:

1. try (executing a code snippet)
2. except (catching the error)
3. else (if try block succeeds)
4. finally (crucial for clean ups like closing a open file after work is done)
"""
import logging as log
try:
    number= int(input("Enter a number only (not zero) = "))
    if number==0:
        raise ZeroDivisionError
    
except ZeroDivisionError as ZDE:#if zero is inputted
    ZDE="Divison by zero"
    print(ZDE)

except ValueError:#if a string or char is inputted
    print("Only Integers except zero please.")

except Exception as e:
    log.exception(e)
    print("This catches any exception like an else statement, so put this at last")

else:
    print(1/number)

#finally executes even after a exeception
finally:
    print("This needs some clean up.")