#Match Case conditions are similar to switch case of C/C++
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
        case _: #default:
            return "Invaild input"
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