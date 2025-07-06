#1D collections 
fruits = ["Apple", "Mango", "Orange"]
vegetables=["Carrot", "Peas", "Potato"]
UPFs=["Chips", "Soda", "Ice-Cream"]

#2D collections
#Examples of 2D collections are:- a list of lists, tuples of tuples and tuples of sets are possible in python
groceries=[fruits, vegetables, UPFs]
            #OR
groceries=[["Apple", "Mango", "Orange"],         
           ["Carrot", "Peas", "Potato"], 
           ["Chips", "Soda", "Ice-Cream"]]
print("To print the 0th row")
print(groceries[0])#prints the 0th row
print("To print the 0th element")
print(groceries[0][0])#prints element at 0th row and at 0th column

print("To print the 2D list")
print(groceries)
print("TO ITERATE OVER EACH ROW")
for collection_of_food in groceries:
    print(collection_of_food)
print("OR")
print("to iterate over the each element, we need nested for/while loop")
for collection_of_food in groceries:
    for food in collection_of_food:
        print(food, end=" ")
    print()

#for taking input for 2D collections
User_2D_List = []#initializing a empty list.
row=int(input("Enter your list row size = "))
column=int(input("Enter your list coloumn size = "))
print(f"Row = {row}, Coloumn = {column}")
for i in range(row):
    temporary_row =[]
    for j in range(column):
        temporary_row.append(int(input()))#temporary row to hold the inputs, Insert method will also work
        print("*", end=" ")
    User_2D_List.append(temporary_row )#the inputted row is now appended to User_2D_List then the list is stored in an another list and then the loop iterates and the value is set again to zero 
    print()
print("Now printing:")
for i in range(row):
    for j in range(column):
        print(User_2D_List[i][j], end=" ")
    print()

array_2D=[]
i=0
j=0
is_loop=True
is_nested_loop=True
while is_loop:
    temporary_row=[]
    while is_nested_loop:
        temporary_row.insert(j, input(f"Element ({i+1},{j+1}) = "))
        if temporary_row[j]=="":
            temporary_row.remove(temporary_row[j])
            break
        j+=1
    array_2D.append(temporary_row)
    user_response=input("Do you want to enter another row? (Enter = yes)")
    if user_response!="":
        is_loop=False
    j=0
    i+=1
for row in array_2D:
    print(row)

user_3D_List=[]
i=int(input("Enter the row size = "))
j=int(input("Enter the max column size = "))
z=int(input("Enter multiple size = "))
for row in range(i):
    temporary_2D_matrix=[]
    for column in range(j):
        temporary_row=[]
        for somthing in range(z):
            temporary_row.append(input(f"Postion {row+1},{column+1},{somthing+1} element = "))
        temporary_2D_matrix.append(temporary_row)
    user_3D_List.append(temporary_2D_matrix)
print("List = ",user_3D_List)

D=[]
max_row=int(input("Enter the number of rows: "))
max_column=int(input("Enter the number of column: "))
max_instances=int(input("Enter the number of instances: "))
row=0
column=0
instance=0
while row<max_row:
    temporary_list=[]
    print("Current row:",row+1)
    column=0
    while column<max_column:
        print("Current column: ", column+1)
        temporary_row=[]
        instance=0
        while instance<max_instances:
            print("Current inst =",instance+1)
            temporary_row.append(int(input(f"Enter a value of cell ({row+1}, {column+1}, {instance+1}) : ")))
            instance+=1
        temporary_list.append(temporary_row)
        column+=1
    D.append(temporary_list)
    row+=1
print(D)