#Reading files of .txt , .json, .csv

file_path="/home/vhvhs/outputOfWrittingFile.txt"
try:
    with open(file_path, 'r') as file:#this a context manager('with', 'as') in this case they auto mate the opening and closing of a file effectively
        content_of_file = file.read()
        print(content_of_file)
except FileNotFoundError:
    print("File not found, Read Error")
except PermissionError:
    print("File Read Error, Permission denied.")
except Exception:
    print("Error occoured.")

import json
print("for json file")
file_path1="/home/vhvhs/OutputOfJsonFile.json"
print()
try:
    with open(file_path1, 'r') as file:
        content_of_json_file = json.load(file)
        print(content_of_json_file)#Prints every thing in the json file till EOF
        print(content_of_json_file["name"])#for printing specific items
        print(content_of_json_file["age"])
        print(content_of_json_file["Profession"])
except FileNotFoundError:
    print("File not found, Read Error")
except PermissionError:
    print("File read permission denied.")
except json.decoder.JSONDecodeError:
    print("Json file decoding failed.")
except Exception:
    print("Error occoured.")

import csv
from itertools import zip_longest
file_path2="/home/vhvhs/OutputOfCSVFile.csv"
try:
    with open(file_path2, 'r') as file_csv_1:
        content_of_csv_file1=file_csv_1.read()#this will read the csv files as just a bunch of strings(like a .txt file)
        print(content_of_csv_file1)
    #or do this
    with open(file_path2, 'r') as file_csv_2:
        content_of_csv_file2=csv.reader(file_csv_2)#this a reader function specifically designed for reading csv files. csv.reader() is an iterator and is memory efficient for reading large csv files as it traverses through line by line and does not load entire content at once
        for row_index, row_data in enumerate(content_of_csv_file2):#enumurate automatically index the row that is being iterated.
            print("[", end="")
            for cell_data in row_data:
                print(f"'{cell_data}'", end=", ")
            print("]")
            #for accessing each element in row_data by its index withoOpenTextMode ut causing error
            for i in range(len(row_data)):
                    print(f"{row_index + 1}: {row_data[i]}")
        # Suppose you expect exactly 3 columns per row:
        for row in content_of_csv_file2:
            a, b, c = zip_longest(row, [], fillvalue=None)
        # Now a, b, c are always defined (possibly None if missing).
            
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("File read permission denied.")
except Exception:
    print("Exception Occured.")


try:
    with open(file_path2, 'r') as file_csv_2:
        csv_content = csv.reader(file_csv_2)
        print("Reading CSV file using csv.reader:")
        for row_number, row_data in enumerate(csv_content):
            print(f"Row {row_number + 1}: {row_data}")
            for row_index, row_data in enumerate(csv_content, start=1):
                print(f"Row {row_index}:", row_data)#raw dump of the row
                for col_index, cell in enumerate(row_data):
                    print(f"  Cell {col_index}: {cell}")# safe—enumerate only gives valid indices

except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'")
except PermissionError:
    print("Error: File read permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")