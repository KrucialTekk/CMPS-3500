# course: CMPS3500
# Asgt: CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 03/27/23  - 04/01/23
# Group 8: Andrew Nguyen, Chidiebere Okpara, Conner Estes, and Noah Malleux
# FILE: ClassProjectGroup8.py
# description: Implementation Basic Data Analysis Routines
# To compile and run python from odin, type 'python3 ClassProjectGroup8.py' or './ClassProjectGroup8.py'

import pandas as pd  # library to search, sort, parse the csv file
import datetime
import numpy
import sys
import traceback
import logging
import csv  # read the csv file(s)
import time  # fine the load time or time to load
import statistics  # statistics of numeric data

try:
    data_frame = None
except OSError as e:
    print("File doesn't exsist: Catching Error")
    print(f"{type(e)}: {e}")
    exit(0)

# [current time] 'YYYY-MM-DD HH:MM:SS.ssssss'
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%H:%M:%S')  # [current time] HH:MM:SS
# This variable is used to hold the correct file name. Set to the first csv file by default, but can be changed to the other csv files in main menu option 1
selectedfile = 'Crime_Data_from_2017_to_2019.csv'

# Function Code Here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def testFunc(num1, num2):
    sum = num1 + num2
    return sum


def counter():  # this doesnt do anything yet
    return 0


def create_array(filename, col_name):
    data = pd.read_csv(filename)
    arr = data[col_name].tolist()
    return arr

# drop elements less than or equal to zero


def drop_zero(arr):
    new_arr = []
    i = 0
    while i < len(arr):
        if arr[i] > 0:
            new_arr.append(arr[i])
        i += 1
    return new_arr


# function for counting elements based on user inputted column

def count_elements(file_path, column_index):
    element_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) > column_index and values[column_index].strip() != '':
                element_count += 1
    return element_count

# unqiue count, does not counnt null, zeros or empty values.


def count_unique_elements(file_path, column_index):
    unique_elements = set()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) > column_index:
                value = row[column_index].strip()
                if value and value != "0" and value.lower() != "null":
                    unique_elements.add(value)
    return len(unique_elements)



# mean

def average(filename, col_name):
    arr = create_array(filename, col_name)
    arr = drop_zero(arr)
    summation = 0
    count = len(arr)
    i = 0
    while i < count:
        summation += arr[i]
        i += 1
    ave = summation/count
    return ave

# mode function or most common


def find_mode(filename, col_name):
    arr = create_array(filename, col_name)
    arr = drop_zero(arr)
    unique_num_list = list(set(arr))
    dictionary = {}
    for i in unique_num_list:
        get_count = arr.count(i)
        dictionary[i] = get_count
    max_repeat = 0
    for i in unique_num_list:
        get_value = dictionary[i]
        if get_value > max_repeat:
            max_repeat = get_value
    result = ''
    for i in unique_num_list:
        if dictionary[i] == max_repeat:
            result = result+str(i)+" "
    return result

# Variance function


def variance(filename, col_name):
    arr = create_array(filename, col_name)
    arr = drop_zero(arr)
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

# Min function


def minimum(filename, col_name):
    arr = create_array(filename, col_name)
    arr = drop_zero(arr)
    max = len(arr) - 1
    min = arr[0]
    i = 0
    while i <= max:
        if arr[i] < min:
            min = arr[i]
        i += 1
    return min

# Max function


def maximum(filename, col_name):
    arr = create_array(filename, col_name)
    arr = drop_zero(arr)
    end = len(arr) - 1
    maximum = arr[0]
    i = 0
    while i <= end:
        if arr[i] > maximum:
            maximum = arr[i]
        i += 1
    return maximum


def find_median(file_path, column_name):
    # mean function or middle: High + low / 2 = middle
    low = minimum(file_path, column_name)
    high = maximum(file_path, column_name)
    median = (high + low) / 2
    return median

def loadingIndicator():
    cnt = 0
    while cnt < 4:
        loadwait = "Now Loading" + "." * cnt
        cnt = cnt + 1;
        print(formatted_time, loadwait, end="\r")
        time.sleep(0.40)
    return 0
# Main Menu++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


print("Main Menu:\n*********")
select = input(
    "(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
while select.isnumeric() != 1:  # Error check is input is not a number
    print("-Input was not valid. Try again.-")
    select = input(
        "(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

while True:
    try:
        pd.set_option('display.max_columns', 30)
        pd.set_option('display.max_rows', 9999999)
        if (select == "1"):
            # if data_frame.empty != True:
            print("Load data set:\n**************")
            print(formatted_time,
                  "Select the numer of the file to load from the list below:")
            # print(" Please select an option:")
            select_file = input(
                " Please select a file: \n[1] Crime_Data_from_2017_to_2019.csv\n[2] Crime_Data_from_2020_to_2021.csv\n[3] Test.csv\n")
            if (select_file == "1"):
                print(formatted_time, "You selected: Option 1")
                loadingIndicator()
                # use this to read the correct file whenever it is needed
                selectedfile = 'Crime_Data_from_2017_to_2019.csv'
                start_time = time.time()
                data_frame = pd.read_csv(selectedfile)
                end_time = time.time()
                load_time = end_time - start_time
                print(formatted_time,'Total columns read: {}'.format(len(data_frame.columns)))
                print(formatted_time,'Total rows read: {}'.format(len(data_frame.index)))
                print("\nFile loaded successfully!")
                print(f'Time to load {load_time:.3f} sec.')
            if (select_file == "2"):
                print(formatted_time, "You selected: Option 1")
                loadingIndicator()
                # use this to read the correct file whenever it is needed
                selectedfile = 'Crime_Data_from_2020_to_2021.csv'
                start_time = time.time()
                data_frame = pd.read_csv(selectedfile)
                end_time = time.time()
                print(formatted_time,'Total columns read: {}'.format(len(data_frame.columns)))
                print(formatted_time,'Total rows read: {}'.format(len(data_frame.index)))
                print("\nFile loaded successfully!")
                print(f'Time to load {load_time:.3f} sec.')
            if (select_file == "3"):
                print(formatted_time, "You selected: Option 1")
                loadingIndicator()
                selectedfile = 'Test.csv'  # use this to read the correct file whenever it is needed
                start_time = time.time()
                data_frame = pd.read_csv(selectedfile)
                end_time = time.time()
                print(formatted_time,'Total columns read: {}'.format(len(data_frame.columns)))
                print(formatted_time,'Total rows read: {}'.format(len(data_frame.index)))
                print("\nFile loaded successfully!")
                print(f'Time to load {load_time:.3f} sec.')
                with open(selectedfile, 'r') as file:  # open and close file
                    print(calltest)

        elif (select == "2"):
            print("Exploring Data: \n******************")
            select_2 = input("(21) List all columns\n(22) Drop Columns\n(23) Describe Columns\n(24) Search Element in Column\n(25) Sort in Ascending/Descending Order \n(26) Select Columns to Display\n(27) Back to Main Menu\n")
            if (select_2 == "21"):
                print('(21) List all columns: \n******************')
                with open('Crime_Data_from_2017_to_2019.csv', 'r') as file:  # open and close file
                    reader = csv.reader(file)  # obj from the csv file
                    columns = next(reader)  # get the row
                    for i, column in enumerate(columns):
                        # print the index of the columns
                        print(f"[{1+i}] <{column} >")

            if (select_2 == "22"):
                print('(22) Drop Columns: \n******************')
                print('List of Columns:')
                for i, column in enumerate(data_frame.columns):
                    # print the index of the columns
                    print(f"[{1+i}] <{column} >")

                drop_input = int(
                    input("Select the desired column you want to drop: "))
                drop_column = data_frame.columns[drop_input - 1]
                data_frame = data_frame.drop(columns=[drop_column])
                print(formatted_time, f' {[drop_input]}')
                print(formatted_time, f' Column {[drop_input]} dropped!')

            if (select_2 == "23"):
                print('(23) Describe Columns: \n******************')
                print(formatted_time, 'Select column number to Describe:\n')
                print(formatted_time, 'Please wait...\n')
                start_time = time.time()
                file_path = 'Crime_Data_from_2017_to_2019.csv'
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    for i, column in enumerate(columns):
                        print(f"[{1+i}] <{column} >")
                selected_column = int(input())
                # Call the count_elements_in_selected_column function to count the elements in the selected column
                # Adjust index since user input is 1-based and Python list indexing is 0-based
                column_index = selected_column - 1
                element_count = count_elements(file_path, column_index)
                # "Stats printed successfully! time to process is {load_time:.3f} sec."
                end_time = time.time()
                load_time = end_time - start_time

                # array of column names
                cols = data_frame.columns
                col_name = cols[column_index]

                col_average = average(file_path, col_name)
                col_sd = standard_deviation(file_path, col_name)
                col_variance = variance(file_path, col_name)
                col_minimum = minimum(file_path, col_name)
                col_maximum = maximum(file_path, col_name)
                col_median = find_median(file_path, col_name)

                # variable that holds the unique elements of the chosen column
                unique_count = count_unique_elements(file_path, column_index)

                print([formatted_time], selected_column)
                print("Column", selected_column, "stats: ")
                print("=========")
                print("Count: ", element_count)
                print("Unqiue: ", unique_count)
                print("Mean: ", col_average)

                # median = find_median(file_path, column_index)
                # print("Median: ", median )
                print("Median: ", col_median)

                # displaying 01/01/2017 12:00:00 AM, and not the number value
                mode = find_mode(file_path, col_name)
                print("Mode: ", mode)
                print("Standard Deviation: ", col_sd)
                print("Variance: ", col_variance)
                print("Minimum: ", col_minimum)
                print("Maximum: ", col_maximum)
                print(
                    f"Stats printed successfully! time to process is {load_time:.3f} sec.")

            if (select_2 == "24"):
                print('(24) Search Element in Column: \n******************')
                print(formatted_time, 'Select column number to perform a search:')
                colnum = 0
                cols = []

                # file does not need to be opened again
                for i, column in enumerate(data_frame.columns):
                    # print the index of the columns
                    print(f"[{1+i}] <{column} >")
                    colnum = colnum +1;

                selectCol = int(input(""))
                while selectCol < 1 or selectCol > colnum:
                    print("Input out of bounds. Try again.")
                    for i, column in enumerate(data_frame.columns):
                        # print the index of the columns
                        print(f"[{1+i}] <{column} >")
                    selectCol = int(input(""))
                print(formatted_time, "You selected column: ", selectCol)
                print(formatted_time, "Enter an element to search")
                selectElement = input("")
                print(formatted_time,
                      f"You selected {selectElement}. Searching...")
                count = 0
                found = "empty"
                start_time = time.time()
                cols = data_frame.iloc[:, selectCol-1].values
                cols = cols.astype(str)
                #print(cols)
                for i in range(len(cols)):
                    if cols[i] == selectElement:
                        found = (selectElement)
                        count = count + 1
              

                end_time = time.time()
                search_time = end_time - start_time
                if (found != "empty"):
                    print(formatted_time, "Element found in", count, "row(s)")
                    print(
                        f"Search was successful! time to process is {search_time:.3f} sec.")
                else:
                    print("Element not found: Heading back to Main Menu\n")
                
            if (select_2 == "25"):
                # sort acending/decending
                print("not implemented")
            if (select_2 == "26"):
                displayinput = int(input("How many columns to display?\n"))
                try:
                    print("Printing your request. (This might take a long time)\n")
                    print(data_frame.head(displayinput))
                except Exception as exc:
                    print("File has not loaded")

            if (select_2 == "27"):
                # Make it when the user selecet 25, it goes back to main
                print('(27)Back to Main Menu: \n******************')
                # select = input("(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

        # example of grouping the csv file for something specific
        # list2 = ["LAT", "LON"]
        # location = data_frame.groupby(["LOCATION"], as_index=False)[list2].count()
        # print(location.head(10))

        elif (select == "3"):  # Data analysis called here
            print('Data Analysis: \n******************')
            print(formatted_time,
                  f'Show the total unique count of crimes per year sorted in descending order.')

            print(formatted_time, f'List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018 in West LA.')

        elif (select == "4"):
            try:
                print("Printing the data_frame. (This takes a long time)")
                print(data_frame.head)
            except Exception as er:
                print("File has not loaded.")

        elif (select == "5"):
            exit(0)
        # else :
        print("\n-Input another valid command-")
        select = input(
            "(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
    except Exception as err:
        print(f"{type(err)}: {err}")
