# course: CMPS3500
# Asgt: CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 03/27/23  - 04/01/23
# Names: Andrew Nguyen, 
# FILE: project3500.py
# description: Implementation Basic Data Analysis Routines
# To compile and run python from odin, type 'python3 project3500.py' or './project3500.py'

import pandas as pd #library to search, sort, parse the csv file
import datetime

#Main menu++++++++++++++++++++++++++++++++++++++++
print("Main Menu:\n*********")
select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
while select.isnumeric() != 1:#Error check is input is not a number
    print("-Input was not valid. Try again.-")
    select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

while True:
    if (select == "1"):
        data_frame = pd.read_csv('Crime_Data_from_2017_to_2019.csv')#read the csv
        if data_frame.empty != True:
            print("File loaded successfully!")
    elif (select == "2"):
        #example of grouping the csv file for something specific
        list2 = ["LAT", "LON"]
        location = data_frame.groupby(["LOCATION"], as_index=False)[list2].count()
        print(location.head(10))
    #elif (select == "3"): #Data analysis called here
    elif (select == "4"):
        print(data_frame.head(5))#this prints 5 lines of data_frame
    elif (select == "5"):
        exit(0)
    print("\n-Input another valid command-")
    select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
