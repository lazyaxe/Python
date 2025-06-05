import random
def gamble_core():
    count=0
    balance=float(input("ENTER YOUR BALANCE: $ "))
    previous_balance=balance
    is_gambling=True
    while is_gambling:
        gambler_confirmation=input("Welcome to the slot machine do want to gamble your grandma's life savings ? ('no/n to quit'):- ")
        if gambler_confirmation.lower() == "n" or gambler_confirmation.lower()=="no":
            print("You escaped, but how long ?")
            is_gambling=False
        else:     
            slot=spin_machine()                         
            print(f"Checking=={slot[0]} :|: {slot[1]} :|: {slot[2]}")
            if slot[0]==slot[1]==slot[2]:
                win(count, balance)
            else:
                lose(count, balance)
    get_payment(balance,previous_balance)
    
def get_payment(balance, previous_balance):
    print(f"your balance is ${balance}")
    if balance<previous_balance:
        print("Grandma's Account's Balance = $ ",balance)
        print("You are in debt bruh")
        gambler_confirmation=input("Pay my debt with more gambling ? ('y/yes to start'):- ")
        if gambler_confirmation.lower() == "y" or gambler_confirmation.lower()=="yes":
            gamble_core()
        else:
            print("then how else are you gonna pay me chum! I'm calling the Police")
            print("----------------------------WASTED------------------------------")
    elif balance>=previous_balance:
        print("Hope you had a great time!")

def spin_machine():
    print("------------------LETS-GO-GAMBLING-------------------")
    fruits=["🍉", "🍓", "🍇"]
    slot = [random.choice(fruits) for _ in range(3)]  # Corrected slot generation
    print("______________________________________")
    print(f"{slot[0]} :|: {slot[1]} :|: {slot[2]}")
    print("______________________________________")
    print()
    print("=======================================================")
    return slot   

def win(balance, count):
    if win_count%3==0:
        print(f"OMG! {win/3:.0f} Gambling Hatrick W bro ! Here's $500")
        balance+=500
    print("Congrats !")
    print("That's a Real Gamblemaxxer !")
    balance+=100
    win_count=count
    win_count+=1        
    print("Grandma's Account's Balance = $ ",balance)
    print(f"Your winning streak = {win_count}")
    return win_count

def lose(balance, count):
    print("Aw, Dang it!")
    balance-=100
    lose_count=count
    lose_count+=1
    print("Grandma's Account's Balance = $ ",balance)
    print(f"Your losing streak = {lose_count}")
    return lose_count
gamble_core()

