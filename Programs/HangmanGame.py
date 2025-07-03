import string
def start_hangman(wins=0, loses=0):
    drawing_progresstion=0
    print("Welcome to hangman!")
    while True:
        print("6 tries left")
        actual_word=input("Start by inputing a letter(whitespace to quit): ")
        actual_word=actual_word.lower()
        print(f"chars are = {len(actual_word)}")
        i=0
        display_letters=[]
        print("Letter to fill:")
        while i<len(actual_word):
            display_letters.append("__")
            print(display_letters[i], end=" ")
            print("This loop should only iterate at the start")
            i+=1
        j=0
        print(f"i={i}, now")
        while True:
            print()
            guess_letter=input("Guess a letter from the blanks:  ")
            #if guess_letter in actual_word :
            #    print(f"{guess_letter} is correct")
            #    print(f"it's indexing is {actual_word.index(guess_letter)+1}")
            #    display_letters[actual_word.index(guess_letter)]= guess_letter
            if guess_letter in actual_word:
                print(f"Correct guess: '{guess_letter}' is in the word!")
                for i in range(len(actual_word)):
                    if actual_word[i] == guess_letter:
                        display_letters[i] = guess_letter
                for display_letter in display_letters:
                    print(display_letter, end=" ")
                if display_letters.count("__")==0:
                    print()
                    print("Congrats on beating hangman!")
                    user_response=input("play again?")
                    if user_response == "":
                        #wins+=1
                        break
                    else:
                        print()
                        return
                        #wins+=1
                print()
                print(f"{display_letters.count("__")} chars remaining....")
            else:
                print(f"{5-drawing_progresstion} tries left...")
                print(f"{display_letters.count("__")} chars remaining....")
                hangman_art = hangman_ascii()
                drawing_progresstion+=1
                print(hangman_art.get(drawing_progresstion))
                if drawing_progresstion==6:#it updates one more 
                    print("YOU LOST !")
                    user_response=input("play again?")
                    if user_response =="":
                        #loses+=1
                        print()
                        break
                    else:
                        print()
                        return
            j+=1


def hangman_ascii():
    art={1: "  O",
        2: "  O\n  |",
        3: "  O\n /|",
        4: "  O\n /|\\",
        5: "  O\n /|\\\n /",
        6: "  O\n /|\\\n / \\"}
    return art

#def hangman_track_record(wins=0,loses=0):
#    count1=wins
#    count2=loses
#    print(f"Wins={count1}")
#    print(f"Loses={count2}")


if __name__ ==  '__main__':
    wins=0
    loses=0
    start_hangman()