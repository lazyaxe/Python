#MEMBERSHIP OPERATORS ARE USED TO FIND A VALUE OR SEQEUNCE IN A STRING TUPLE LIST SET OR DICTIONARY
# MEMBERSHIP OPERATORS ARE : 'in' AND 'not in' 

word=input("Enter a word = ")
letter = input("Guess the letter of the word:")
if letter in word:
    print(f"The {letter} in the word !")
elif letter not in word:
    print(f"The {letter} not in the word")
else:
    print("incorrect word")


letters=[]
is_loop=True
while is_loop:
    print("Guess the word.")
    temp_letter=input("Enter a letter = ")
    if temp_letter in word:#'in' returns a boolean(True) if the letter is found
        print("Congrats!")
        letters.append(temp_letter)
        print("List of Correct guesses = ", letters)
        if len(letters)==len(word):
            print("Congrats, You beat the game!")
            print("The word was:", word)
            is_loop=False
    else:
        print("try again,")
        print("List of Correct guesses = ", letters)

print("FOR LISTS/TUPLES/SETS")
students = {"Larry", "Joe", "John"}
student_name=input("Check Student's names:")
if student_name in students:
    print("Student name found in data set")
elif student_name not in students:#'not in' returns a boolean(True) if the letter is not found.
    print("Student name not found!")
else:
    print("Something went wrong in input process...")

print("FOR DICTIONARIES")
student_grades={"Larry":"A",
        "Joe"  :"B",
        "John" :"F"}
student_name = input("Enter a students name to check their grades: ")
if not student_name in student_grades:# this will check IF student_name IS NOT EQUAL TO KEYS will work the same with the student_grades.key()
    print("name not found")
elif student_name in student_grades:
    print(f"{student_name}'s grade is {student_grades[student_name]}.")

print("For STRs")
user_email=input("Make a new email: ")
if "@" and "." in user_email:
    print(f"{user_email} is valid")
else:
    print("Missing @ or . (or both) in email")

