# course: CMPS3500
# Asgt: CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 03/27/23  - 04/01/23
# Names: Andrew Nguyen
# FILE: project3500.py
# description: Implementation Basic Data Analysis Routines
# To compile and run python from odin, type 'python3 project3500.py' or './project3500.py'

import pandas as pd #library to search, sort, parse the csv file

#Various tests
hello = 'hi guys'
myList = [1,2,3]
print(hello)
print(myList[1])

data_frame = pd.read_csv('Crime_Data_from_2017_to_2019.csv')#read the csv
print(data_frame.head(5))#this prints 5 lines of data_frame

list2 = ["LAT", "LON"]
#example of grouping the csv file for something specific
location = data_frame.groupby(["LOCATION"], as_index=False)[list2].count()
print(location.head(10))


