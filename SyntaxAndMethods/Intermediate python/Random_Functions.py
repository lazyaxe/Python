import random
#print(help(random)) for help if you forgot methods names

minimum_value=1
maximum_value=100

#setting a range of min and max value limit of randint function
print("FOR INTEGERS")
number=random.randint(minimum_value, maximum_value)#random is the module and randint is the method
print(number)

#for the floating point
print("FOR FLOATING INTEGERS")  
number2=random.random()
print(number2)

#for randomized choice strings
print("FOR LISTS, TUPLES")
options=("rock", "paper", "scissors")#using a tuple
option= random.choice(options)

print("FOR SHUFFLING A LIST'S ORDER" )
cards=["1", "2", "3", "4", "5", "6", "J", "K", "A"]# A list
random.shuffle(cards)#passing the list of cards in a ordered sequence
print(cards)#now cards are shuffled i.e. list is now randomly ordered 
