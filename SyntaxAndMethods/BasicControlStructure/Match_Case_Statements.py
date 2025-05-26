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
        case 7:
            return "Saturday"
        case _: #default:
            return "Invaild input"
is_loop = True
while is_loop:
    day = input("Enter a day: ")
    if (day.lower()=="e"):
        print("Exiting.....")
        is_loop=False
    else:
        day = int(day)
        day=day%7
        print(day_of_the_week(day))