# MATCH-CASES:
"""
    ~> Match-cases are very similar in terms of functionality in comparasion to if-elif-else statements as it also manipules the control flow.
    ~> Match Cases are equivalent to switch cases in C/C++.
    ~> They are preffered when there is a need of discrete comparision or where inequality operators are not needed
"""
def day_of_the_week(input_day):
    match input_day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tueday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 0: # because 7 % 7 = 0
            return "Saturday"
        case _: # default case, similar to else
            return "Invaild input"
"""
Equivalent if else ladder:

if input_day == 1:
    return "Sunday"
elif input_day == 2:
    return "Monday"
elif input_day == 3:
    return "Tuesday"
elif input_day == 4:
    return "Wednesday"
elif input_day == 5:
    return "Thrusday"
elif input_day == 6:
    return "Friday"
elif input_day == 7:
    return "Saturday"
else:
    return "Invaild Input"
"""


input_day = input("Enter a day: ")
if not input_day.isdigit():
    print("Invaild Input")
else:
    input_day = int(input_day)
    if input_day <= 0:
        print("Invaild Input")
    else:
        input_day %= 7
        print(day_of_the_week(input_day))