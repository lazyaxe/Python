# READING .txt , .json, .csv FILES in Python:
"""
~> Files in Python can be usually accessed by:
1. Using manual open(file, mode) method
2. Using Pythonic Context Managers i.e. automate file opening and closing.

There are 4 read modes in Python
1. 'r' : read-only
2. 'r+' : read and write, creates a new file if not found 
3. 'rb' : read binary only
4. 'rb+' : read and write binary, creates a new file if not found
"""

#1. Text files
txt_file_path = "/home/vhvhs/outputOfWrittingFile.txt"

try:
    txt_file = open(file = txt_file_path, mode = 'r')

except FileNotFoundError:
    print("File not found, Read Error")

except PermissionError:
    print("File Read Error, Permission denied.")

except Exception:
    print("Error occoured.")

else:
    print("File read successfully ")
    content_of_txt_file = txt_file.read()
    print(content_of_txt_file)

finally:
    print("Execution Completed")


#2. JSON(JavaScript Object Notation) files
import json

print("For JSON files:")
json_file_path = "/home/vhvhs/OutputOfJsonFile.json"
print()

#A context manager('with', 'as') in this case is used to automate the opening and closing of a file effectively. No need for manual execption handling.
with open(file = json_file_path, mode = 'r') as json_file:
    #load() To read a JSON
    content_of_json_file = json.load(json_file)
    
    #Prints every thing in the json file till EOF
    print(content_of_json_file)
    
    # Or print selected (data is stored as a dict in JSON)
    print(content_of_json_file["name"])
    print(content_of_json_file["age"])
    print(content_of_json_file["Profession"])

#3. For CSV(Comma Separated Values)
import csv
from itertools import zip_longest

csv_file_path = "/home/vhvhs/OutputOfCSVFile.csv"

with open(file = csv_file_path, mode = 'r') as file_csv_1:
    #this will read the csv files as just a bunch of strings(like a .txt file)
    content_of_csv_file1 = file_csv_1.read()
    print(content_of_csv_file1)


"""
Alternatively,
    ~> csv.reader method is specifically made for reading csv files. 
    ~> csv.reader() is an iterator and is memory efficient for reading large csv files as it traverses through line by line and does not load entire content at once.
"""
with open(file = csv_file_path, mode = 'r') as file_csv_2:
    content_of_csv_file2 = csv.reader(file_csv_2)

    print(content_of_csv_file2)

    #enumurate automatically index the row that is being iterated.
    for row_index, row_data in enumerate(content_of_csv_file2):
        print("[", end = "")
        for cell_data in row_data:
            print(f"'{cell_data}'", end = ", ")
        print("]")

        #for accessing each element in row_data by its index withOpenTextMode ut causing error
        for i in range(len(row_data)):
                print(f"{row_index + 1}: {row_data[i]}")

    # Suppose you expect exactly 3 columns per row:
    for row in content_of_csv_file2:
        a, b, c = zip_longest(row, [], fillvalue = None)
        # Now a, b, c are always defined (possibly None if missing).
            

with open(file = csv_file_path, mode = 'r') as file_csv_2:
    csv_content = csv.reader(file_csv_2)
    print("Reading CSV file using csv.reader:")
    
    # What is enumarate function?
    """
    
    """
    for row_number, row_data in enumerate(csv_content):
        print(f"Row {row_number + 1}: {row_data}")
        for row_index, row_data in enumerate(csv_content, start = 1):
            print(f"Row {row_index}:", row_data)#raw dump of the row
            for col_index, cell in enumerate(row_data):
                print(f"  Cell {col_index}: {cell}")# safe—enumerate only gives valid indices
