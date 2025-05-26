#writing files in python (.txt, .json, .csv)

txt_data = "I like pizza!"

file_path = "/home/vhvhs/outputOfWrittingFile.txt"

with open(file_path, "w") as file:# with is statement used to wrap the code i.e. closes the file as soon as it's done reading
    # open(), the first parameter will return as the file object 
    # the second parameter, "w" is the writing mode
        file.write(txt_data)
        print(f"text file {file_path} is created now")

try:
    with open(file_path, "x") as file:# with is statement used to wrap the code i.e. closes the file as soon as it's done reading
    # open(), the first parameter will return as the file object 
    # the second parameter, "w" is the writing mode
    #it will throw an error if the file already exists
        file.write(txt_data)
        print(f"text file {file_path} is created now")

except FileExistsError:
    print("This file exists already.")

finally:
    print("For appending/updating a file's data. ")
    txt_data2 = "I also like Healthy Food!"

    with open(file_path, "a") as file:
        file.write("\n"+txt_data2+"\n")
        print(f"text file {file_path} is appended/updated now")

    #for lists 
    print("For appending/updating a file's data.")
    employee_list = ["Eugene", "Mayweather", "Sourbee"]

    with open(file_path, "a") as file:
        for employee in employee_list:
            file.write(employee+"\n")
        print(f"text file {file_path} is appended/updated now for the list")

import json

print("For the json file.")#Json needs couples of key and values i.e. a dictionary

employee_details = {"name":"SpongeBob SquarePants",
            "age":12,
            "Job/Profession":"Cook"}

file_path2 = "/home/vhvhs/OutputOfJsonFile.json"

with open(file_path2, "w") as file:
        for key, value in employee_details.items():
            file.write(f"{key}={value}\n")
        print(f"Json file {file_path2} is created now")

import csv

print("For .csv files")
#csv = comma separated values, they for data spreadsheets like Microsoft excel or Google Sheets

employee_2D_collection = [["Name", "Age", "Profession"],
                          ["Harsh", "18", "Unemployed"],
                          ["Mango", "0", "Fruit"]] 

file_path2 = "/home/vhvhs/OutputOfCSVFile.csv"

with open(file_path2, "w") as file:
        
        writer = csv.writer(file)

        for employee_row in employee_2D_collection:
            writer.writerow(employee_row)
        print(f"CSV file {file_path2} is created now")

    


