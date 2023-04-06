# course: CMPS3500
# Asgt: CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 03/27/23  - 04/01/23
# Group 8: Andrew Nguyen, Chidiebere Okpara, Conner Estes, and Noah Malleux 
# FILE: ClassProjectGroup8.py
# description: Implementation Basic Data Analysis Routines
# To compile and run python from odin, type 'python3 ClassProjectGroup8.py' or './ClassProjectGroup8.py'

import pandas as pd # library to search, sort, parse the csv file
import datetime
import numpy 
import sys
import traceback
import logging
import csv # read the csv file(s)
import time # fine the load time or time to load 
import statistics # statistics of numeric data: mean, mode

try:
    data_frame = pd.read_csv('Crime_Data_from_2017_to_2019.csv')# read the csv (move these from local to global)
except OSError as e:
    print("File doesn't exsist: Catching Error")
    print(f"{type(e)}: {e}")
    exit(0)
     
current_time = datetime.datetime.now()# [current time] 'YYYY-MM-DD HH:MM:SS.ssssss'
formatted_time = current_time.strftime('%H:%M:%S') # [current time] HH:MM:SS
selectedfile = 'Crime_Data_from_2017_to_2019.csv'# This variable is used to hold the correct file name. Set to the first csv file by default, but can be changed to the other csv files in main menu option 1

# Function Code Here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def testFunc(num1, num2):
    sum = num1 + num2
    return sum

def counter(): #this doesnt do anything yet
    return 0

def create_array(filename,col_name):
  data = pd.read_csv(filename)
  arr = data[col_name].tolist()
  return arr

# function for counting elements based on user inputted column
def count_elements(file_path, column_index ):
    element_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) > column_index:
                element_count += 1
    return element_count

# unqiue 
def count_unique_elements(file_path, column_index):
    unique_elements = set()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) > column_index:
                unique_elements.add(row[column_index])
    return len(unique_elements)

# mean
def average(filename, col_name):
  arr = create_array(filename,col_name)
  summation = 0
  count = len(arr)
  i = 0
  while i < count:
    summation += arr[i]
    i += 1
  ave = summation/count
  return ave

# mode function or most common

# Variance function 
def variance(filename, col_name):
  arr = create_array(filename,col_name)
  ave = average(filename, col_name)
  pop_size = len(arr)
  summation = 0
  i = 0
  while i < pop_size:
    value = arr[i]
    summation += (value - ave)**2
    i += 1
  variance = (summation/pop_size)
  return variance

# Standarad Deviation (SD)
def standard_deviation(filename, col_name):
  radicand = variance(filename, col_name)
  sd = radicand**(1/2)
  return sd

# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

# Min function
def minimum(filename, col_name):
  arr = create_array(filename,col_name)
  max = len(arr) - 1
  quicksort(arr, 0, max)
  min = arr[0]
  return min

# Max function 
def maximum(filename, col_name):
  arr = create_array(filename,col_name)
  max = len(arr) - 1
  quicksort(arr, 0, max)
  maximum = arr[max]
  return maximum

def find_median(file_path, column_name):  
  # mean function or middle: High + low / 2 = middle
  low = minimum(file_path, column_name)
  high = maximum(file_path, column_name)
  median = (high + low) / 2
  return median

""""
#def find_median( file_path, column_index ): # mean function or middle: High + low / 2 = middle 
    #with open(file_path, 'r') as file:
        #reader = csv.reader(file)
        #next(reader)
        #values = []
        #for row in reader:
            #for item in row:
                #try:
                    #values.append(float(item))
                #except ValueError:
                    #pass
        #return statistics.median(values)
# median = find_median(file_path, selected_column )
                #print("Median: ", median )
"""

# Main Menu++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("Main Menu:\n*********")
select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
while select.isnumeric() != 1:# Error check is input is not a number
    print("-Input was not valid. Try again.-")
    select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

while True:
    try:
        if (select == "1"):
            if data_frame.empty != True:
                print("Load data set:\n**************")
                print(formatted_time,"Select the numer of the file to load from the list below:")
                # print(" Please select an option:")
                select_file = input(" Please select a file: \n[1] Crime_Data_from_2017_to_2019.csv\n[2] Crime_Data_from_2020_to_2021.csv\n[3] Test.csv\n")
            if(select_file == "1"):
                print(formatted_time,"You selected: Option 1")
                selectedfile = 'Crime_Data_from_2017_to_2019.csv'#use this to read the correct file whenever it is needed
                start_time = time.time()
                # with open('Crime_Data_from_2017_to_2019.csv', 'r') as file: #open and close file
                with open(selectedfile, 'r') as file: # open and close file
                    reader = csv.reader(file) # obj from the csv file
                    header = next(reader) # get the row
                    col = len(header) # count the number of colums in the row
                    row = sum(1 for row in reader) # add the number of rows 
                    for row in reader:
                     pass
                end_time = time.time()
                load_time = end_time - start_time
                print(formatted_time,f'Total columns read: {col}')
                print(formatted_time,f'Total rows read: {row}')
                print("\nFile loaded successfully!")
                print(f'Time to load {load_time:.3f} sec.')
            if(select_file == "2"):
                print("Code to load file [2] not implemented yet")
                selectedfile = 'Crime_Data_from_2020_to_2021.csv'# use this to read the correct file whenever it is needed
            if(select_file == "3"):
                print("Code to load file [3] not implemented yet\n")
                selectedfile = 'Test.csv'# use this to read the correct file whenever it is needed

                calltest = testFunc(3,6)
                print(calltest)
                with open(selectedfile, 'r') as file: # open and close file
                    print(calltest)

        elif (select == "2"):
            print("Exploring Data: \n******************")
            select_2 = input("(21) List all columns:\n(22) Drop Columns:\n(23) Describe Columns:\n(24) Search Element in Column:\n(25) Back to Main Menu\n")
            if (select_2 == "21"):
                print('(21) List all columns: \n******************')
                with open('Crime_Data_from_2017_to_2019.csv', 'r') as file: # open and close file
                    reader = csv.reader(file) # obj from the csv file
                    columns = next(reader) # get the row
                    for i, column in enumerate(columns):
                        print(f"[{1+i}] <{column} >") # print the index of the columns 

            if (select_2 == "22"):
                print('(22) Drop Columns: \n******************')
                print('Select a column number to Drop from the list:')
                with open('Crime_Data_from_2017_to_2019.csv', 'r') as file: # open and close file and display the columns 
                    reader = csv.reader(file) # obj from the csv file
                    columns = next(reader) # get the row
                    for i, column in enumerate(columns):
                        print(f"[{1+i}] <{column} >") # print the index of the columns 
            
                drop_column = int(input("Select the desired column you want to drop: "))# drop columns 

                with open('Crime_Data_from_2017_to_2019.csv', 'r') as file_in, open('new_Crime_Data_from_2017_to_2019.csv', 'w', newline='' ) as file_out:
                    reader = csv.reader(file_in) # read to csv file 
                    writer = csv.writer(file_out) # write to csv file 
                    for row in reader:
                        del row[drop_column]
                        writer.writerow(row)

                print(formatted_time,f' {[drop_column]}')
                print(formatted_time,f' Column {[drop_column]} dropped!')

            if (select_2 == "23"):
                print('(23) Describe Columns: \n******************')
                print(formatted_time,'Select column number to Describe:\n') 
                start_time = time.time()
                file_path = 'Crime_Data_from_2017_to_2019.csv'
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    for i, column in enumerate(columns):
                        print(f"[{1+i}] <{column} >")
                selected_column = int(input())
                # Call the count_elements_in_selected_column function to count the elements in the selected column
                column_index = selected_column - 1  # Adjust index since user input is 1-based and Python list indexing is 0-based
                element_count = count_elements(file_path, column_index)
                end_time = time.time() # "Stats printed successfully! time to process is {load_time:.3f} sec."
                load_time = end_time - start_time # 
                
                # array of column names
                cols = data_frame.columns
                col_name = cols[column_index]
                
                #variable that holds the unique elements of the chosen column
                unique_count = count_unique_elements(file_path, column_index)
                
                print([formatted_time], selected_column)
                print("Column", selected_column, "stats: " )
                print("=========")
                print("Count: ",element_count)
                print("Unqiue: ", unique_count)
                print("Mean: ")

                # key error
                #median = find_median(file_path, column_index)
                #print("Median: ", median )
                print("Mode: ")

                print("Standard Deviation: ")
                print("Variance: ")

                print("Minimum: ")
                print("Maximum: ")

                print(f"Stats printed successfully! time to process is {load_time:.3f} sec.")

            if (select_2 == "24"):
                print('(24) Search Element in Column: \n******************')
                print(formatted_time, 'Select column number to perform a search:') 

                with open('Crime_Data_from_2017_to_2019.csv', 'r') as file: # open and close file and display the columns 
                    reader = csv.reader(file) # obj from the csv file
                    columns = next(reader) # get the row
                    for i, column in enumerate(columns):
                        print(f"[{1+i}] <{column} >") # print the index of the columns 

                selectCol = int(input(""))
                print(formatted_time, "You selected column: ", selectCol)
                print(formatted_time, "Enter an element to search")  
                selectElement = int(input(""))
            
                data_frame.loc[selectElement]
                # help me
                # rows = []
                # with open('Crime_Data_from_2017_to_2019.csv', 'r') as file_in, open('new_Crime_Data_from_2017_to_2019.csv', 'w', newline='' ) as file_out:
                    # reader = csv.reader(file_in) #read to csv file 
                    # writer = csv.writer(file_out) #write to csv file 
                    # for row in reader:
                        # Ret = row[selectCol]
                        # if row == selectElement:
                            # myRet = selectElement
                            # print(formatted_time, row)
                    # else :
                        # myRet = 0
                        # print("Element not found in Column: ", selectCol)

                # if myRet == 0:
                # print("Element not found in Column: ", selectCol)
           # else :
                print(formatted_time)

            if (select_2 == "25"):
                print('(25)Back to Main Menu: \n******************') # Make it when the user selecet 25, it goes back to main
                # select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

        # example of grouping the csv file for something specific
        # list2 = ["LAT", "LON"]
        # location = data_frame.groupby(["LOCATION"], as_index=False)[list2].count()
        # print(location.head(10))

        # elif (select == "3"): # Data analysis called here
        elif (select == "4"):
            print(data_frame.head(5)) # this prints 5 lines of data_frame
        elif (select == "5"):
            exit(0)
        # else :
        print("\n-Input another valid command-")
        select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
    except Exception as err:
        print(f"{type(err)}: {err}")
