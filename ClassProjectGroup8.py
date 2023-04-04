# course: CMPS3500
# Asgt: CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 03/27/23  - 04/01/23
# Group 8: Andrew Nguyen, Chidiebere Okpara, Conner Estes, and Noah Malleux 
# FILE: ClassProjectGroup8.py
# description: Implementation Basic Data Analysis Routines
# To compile and run python from odin, type 'python3 ClassProjectGroup8.py' or './ClassProjectGroup8.py'

import pandas as pd #library to search, sort, parse the csv file
import datetime
import numpy 
import csv #read the csv file(s)
import time #fine the load time or time to load 

#Main menu++++++++++++++++++++++++++++++++++++++++
data_frame = pd.read_csv('Crime_Data_from_2017_to_2019.csv')#read the csv (move these from local to global)
current_time = datetime.datetime.now()#[current time] 'YYYY-MM-DD HH:MM:SS.ssssss'
formatted_time = current_time.strftime('%H:%M:%S') #[current time] HH:MM:SS
print("Main Menu:\n*********")
select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
while select.isnumeric() != 1:#Error check is input is not a number
    print("-Input was not valid. Try again.-")
    select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

while True:
    if (select == "1"):
        #data_frame = pd.read_csv('Crime_Data_from_2017_to_2019.csv')#read the csv
        #current_time = datetime.datetime.now()#[current time] 'YYYY-MM-DD HH:MM:SS.ssssss'
        #formatted_time = current_time.strftime('%H:%M:%S') #[current time] HH:MM:SS
        if data_frame.empty != True:
            print("Load data set:\n**************")
            print(formatted_time,"Select the numer of the file to load from the list below:")
            print(" Please select an option:")
            print(" [1] Crime_Data_from_2017_to_2019.csv")
        if(select == "1"):
            print(formatted_time,"1")
            start_time = time.time()
            with open('Crime_Data_from_2017_to_2019.csv', 'r') as file: #open and close file
                reader = csv.reader(file) #obj from the csv file
                header = next(reader) #get the row
                col = len(header) #count the number of colums in the row
                row = sum(1 for row in reader) #add the number of rows 
                for row in reader:
                 pass
            end_time = time.time()
            load_time = end_time - start_time
            print(formatted_time,f'Total columns read: {col}')
            print(formatted_time,f'Total rows read: {row}')
            print("\nFile loaded successfully!")
            print(f'Time to load {load_time:.3f} sec.')

    elif (select == "2"):
        print("Exploring Data: \n******************")
        select_2 = input("(21) List all columns:\n(22) Drop Columns:\n(23) Describe Columns:\n(24) Search Element in Column:\n(25) Back to Main Menu\n")
        if (select_2 == "21"):
            print('(21) List all columns: \n******************')
            with open('Crime_Data_from_2017_to_2019.csv', 'r') as file: #open and close file
                reader = csv.reader(file) #obj from the csv file
                columns = next(reader) #get the row
                for i, column in enumerate(columns):
                    print(f"[{1+i}] <{column} >") #print the index of the columns 

        if (select_2 == "22"):
            print('(22) Drop Columns: \n******************')
            print('Select a column number to Drop from the list:')
            with open('Crime_Data_from_2017_to_2019.csv', 'r') as file: #open and close file and display the columns 
                reader = csv.reader(file) #obj from the csv file
                columns = next(reader) #get the row
                for i, column in enumerate(columns):
                    print(f"[{1+i}] <{column} >") #print the index of the columns 
            
            drop_column = int(input("Select the desired column you want to drop: "))#drop columns 

            with open('Crime_Data_from_2017_to_2019.csv', 'r') as file_in, open('new_Crime_Data_from_2017_to_2019.csv', 'w', newline='' ) as file_out:
                reader = csv.reader(file_in) #read to csv file 
                writer = csv.writer(file_out) #write to csv file 
                for row in reader:
                    del row[drop_column]
                    writer.writerow(row)

            print(formatted_time,f' {[drop_column]}')
            print(formatted_time,f' Column {[drop_column]} dropped!')

        if (select_2 == "23"):
            print('(23) Describe Columns: \n******************')
            print(formatted_time,'Select column number to Describe:\n') 
            print('Select a column to Drop from the list:')

        if (select_2 == "24"):
            print('(24) Search Element in Column: \n******************')
            print(formatted_time, 'Select column number to perform a search:\n') 
            print('Select a column to Drop from the list:')

        if (select_2 == "25"):
            print('(25)Back to Main Menu: \n******************') # Make it when the user selecet 25, it goes back to main
            select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

        #example of grouping the csv file for something specific
        #list2 = ["LAT", "LON"]
        #location = data_frame.groupby(["LOCATION"], as_index=False)[list2].count()
        #print(location.head(10))
    #elif (select == "3"): #Data analysis called here
    elif (select == "4"):
        print(data_frame.head(5))#this prints 5 lines of data_frame
    elif (select == "5"):
        exit(0)
    print("\n-Input another valid command-")
    select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
