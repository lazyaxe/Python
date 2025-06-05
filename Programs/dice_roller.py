import random
#making up a dictionary 
dice_art={
     1:("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
     2:("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
     3:("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
     4:("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
     5:("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
     6:("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
        }
dice=[]
is_playing = True
while is_playing:
    number_of_dice = int(input("Number of rolling dices: "))
    total=0
    for die in range(number_of_dice):
        dice.append(random.randint(1,6))#adds a random number to each item on dice list
    user_input=input("Vertical(v) or Horizontal(h)")
    
    if user_input.lower()=="v":

        for die in range(0,number_of_dice):
            for value in dice_art.get(dice[die]):
                print(f"{value}")
        print()

    elif user_input.lower()=="h":

        for new_line in range(5):
            for die in dice:#die stores the nth value of nth item in dice list
                print(dice_art.get(die)[new_line], end="")#.get fetches the value of die i.e 1 or 5 etc.. and uses it as key for dice-art dictionary and the value of dice_art is a tuple so the x_th value row is printed of all keys
            print()
    else:
        print("enter the correct response please")
    for die in dice:
        total+=die
    print(f"Total = {total}")
    print()
    user_input=input("Play again?(y)/(n)")
    if user_input.lower()=="n":
        print("You exited the game")
        is_playing=False
