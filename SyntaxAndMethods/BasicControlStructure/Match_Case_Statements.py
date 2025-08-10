"""
Match-Cases:

    Match-cases are very similar in terms of functionality in comparasion to if-elif-else statements as it also manipules the control flow.

    Match Case conditions are equivalent to switch case in C/C++.
"""

def day_of_the_week(day):
    match day:
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
        case 0: #because 7%7=0
            return "Saturday"
        case _: #default case, similar to else
            return "Invaild input"
"""
equivalent if else ladder:

if day=="Sunday":    
    return 1
elif day=="Monday":
    return 2
elif day=="Tuesday":
    return 3
elif day=="Wednesday":
    return 4
elif day=="Thrusday":
    return 5
elif day=="Friday":
    return 6
elif day=="Saturday":
    return 7
else: 
    return "Invaild input"
"""
is_loop = True
while is_loop:
    day = input("Enter a day: ")
    if (day.lower()=="e"):
        print("Exiting.....")
        is_loop=False
    elif not day.isdigit():
        print("Invaild Input")
    else:
        day=int(day)
        if day<=0:
            print("Invaild Input")
        else:
            day%=7
            print(day_of_the_week(day))