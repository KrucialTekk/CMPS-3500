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
import csv  
import time  
import statistics  
from collections import Counter

try:
    data_frame = None
except OSError as e:
    print("File doesn't exsist: Catching Error")
    print(f"{type(e)}: {e}")
    exit(0)


current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%H:%M:%S') 
formatted_time2 = "%m/%d/%Y %I:%M:%S %p"
selectedfile = 'Crime_Data_from_2017_to_2019.csv'

# Function Code Here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def testFunc(num1, num2):
    sum = num1 + num2
    return sum


def counter():  
    return 0


def create_array(data, col_name):
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

def count_elements(data_frame, column_name):
    if data_frame[column_name].dtype == 'object':
        arr = data_frame[column_name].tolist()
    else:
        arr = drop_zero(create_array(data_frame, column_name))
    element_count = len(arr)
    return element_count

# unqiue


def count_unique_elements(data_frame, column_name):
    if data_frame[column_name].dtype == 'object':
        arr = data_frame[column_name].tolist()
    else:
        arr = drop_zero(create_array(data_frame, column_name))
    unique_elements = set(arr)
    unique_count = len(unique_elements)
    return unique_count

# mean


def average(data, col_name):
    arr = create_array(data, col_name)
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


def find_mode(data, col_name):
    arr = create_array(data, col_name)
    arr = drop_zero(arr)
    c = Counter(arr)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

# Variance function


def variance(data, col_name):
    arr = create_array(data, col_name)
    arr = drop_zero(arr)
    ave = average(data, col_name)
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


def standard_deviation(data, col_name):
    radicand = variance(data, col_name)
    sd = radicand**(1/2)
    return sd

# Min function


def minimum(data, col_name):
    arr = create_array(data, col_name)
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


def maximum(data, col_name):
    arr = create_array(data, col_name)
    arr = drop_zero(arr)
    end = len(arr) - 1
    maximum = arr[0]
    i = 0
    while i <= end:
        if arr[i] > maximum:
            maximum = arr[i]
        i += 1
    return maximum


def find_median(data, column_name):
    # mean function or middle: High + low / 2 = middle
    low = minimum(data, column_name)
    high = maximum(data, column_name)
    median = (high + low) / 2
    return median


def loadingIndicator():
    cnt = 0
    while cnt < 4:
        loadwait = "Now Loading" + "." * cnt
        cnt = cnt + 1
        print(formatted_time, loadwait, end="\r")
        time.sleep(0.425)
    return 0

#(3) Data Analysys
def crimes_by_year(file_path):

    df = pd.read_csv(file_path)
    df['Date Rptd'] = pd.to_datetime(df['Date Rptd'])
    df['Year'] = df['Date Rptd'].dt.year
    # Column not found: Crime
    crimes_per_year = df.groupby('Year')['Crime'].nunique()
    crimes_per_year = crimes_per_year.sort_values(ascending = False)
    result_df = pd.DataFrame({'Year': crimes_per_year.index, 'Total Unique Crimes': crimes_per_year.values})

    print(result_df)
    return result_df

# Main Menu++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


print("Main Menu:\n*********")
select = input(
    "(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
while select.isnumeric() != 1:  
    print("-Input was not valid. Try again.-")
    select = input(
        "(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")

while True:
    try:
        pd.set_option('display.max_columns', 30)
        pd.set_option('display.max_rows', 9999999)
        if (select == "1"):
           
            print("Load data set:\n**************")
            print(formatted_time,
                  "Select the numer of the file to load from the list below:")
          
            select_file = input(
                "Please select a file: \n[1] Crime_Data_from_2017_to_2019.csv\n[2] Crime_Data_from_2020_to_2021.csv\n[3] Test.csv\n")
            if (select_file == "1"):
                print(formatted_time, "You selected: Option 1")
                loadingIndicator()
                selectedfile = 'Crime_Data_from_2017_to_2019.csv'
                start_time = time.time()
                data_frame = pd.read_csv(selectedfile)
                data_frame = data_frame.drop(['Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street'],  axis='columns')
                end_time = time.time()
                load_time = end_time - start_time
                print(formatted_time, 'Total columns read: {}'.format(
                    len(data_frame.columns)))
                print(formatted_time, 'Total rows read: {}'.format(
                    len(data_frame.index)))
                print("\nFile loaded successfully!")
                print(f'Time to load {load_time:.3f} sec.')
            if (select_file == "2"):
                print(formatted_time, "You selected: Option 1")
                loadingIndicator()
              
                selectedfile = 'Crime_Data_from_2020_to_2021.csv'
                start_time = time.time()
                data_frame = pd.read_csv(selectedfile)
                end_time = time.time()
                print(formatted_time, 'Total columns read: {}'.format(
                    len(data_frame.columns)))
                print(formatted_time, 'Total rows read: {}'.format(
                    len(data_frame.index)))
                print("\nFile loaded successfully!")
                print(f'Time to load {load_time:.3f} sec.')
            if (select_file == "3"):
                print(formatted_time, "You selected: Option 1")
                loadingIndicator()
                selectedfile = 'Test.csv'  
                start_time = time.time()
                data_frame = pd.read_csv(selectedfile)
                end_time = time.time()
                print(formatted_time, 'Total columns read: {}'.format(
                    len(data_frame.columns)))
                print(formatted_time, 'Total rows read: {}'.format(
                    len(data_frame.index)))
                print("\nFile loaded successfully!")
                print(f'Time to load {load_time:.3f} sec.')
                with open(selectedfile, 'r') as file:  
                    print(calltest)

        elif (select == "2"):
            print("Exploring Data: \n******************")
            select_2 = input("(21) List all columns\n(22) Drop Columns\n(23) Describe Columns\n(24) Search Element in Column\n(25) Sort in Ascending/Descending Order \n(26) Select Columns to Display\n(27) Back to Main Menu\n")
            if (select_2 == "21"):
                print('(21) List all columns: \n******************')
                with open('Crime_Data_from_2017_to_2019.csv', 'r') as file:  
                    for i, column in enumerate(data_frame.columns):
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
                for i, column in enumerate(data_frame.columns):
                    # print the index of the columns
                    print(f"[{1+i}] <{column} >")
                selected_column = int(input())
                column_index = selected_column - 1

                # array of column names
                cols = data_frame.columns
                col_name = cols[column_index]
                # Call the count_elements_in_selected_column function to count the elements in the selected column
                

                print([formatted_time], selected_column)
                print("Column", selected_column, "stats: ")
                print("=====================")
                print("[Press 'Ctrl + C' if computation takes too long!]")
                start_time = time.time()
                try:
                    element_count = count_elements(data_frame, col_name)
                    print("Count: ", element_count)
                except:
                    print("Count: Not applicable")
                try:
                    unique_count = count_unique_elements(
                        data_frame, col_name)
                    print("Unqiue: ", unique_count)
                except:
                    print("Unqiue: Not applicable")
                try:
                    col_average = average(data_frame, col_name)
                    print("Mean: ", col_average)
                except:
                    print("Mean: Not applicable")
                try:
                    col_sd = standard_deviation(data_frame, col_name)
                    print("Standard Deviation: ", col_sd)
                except:
                    print("Standard Deviation: Not applicable")
                try:
                    col_variance = variance(data_frame, col_name)
                    print("Variance: ", col_variance)
                except:
                    print("Variance: Not applicable")
                try:
                    col_minimum = minimum(data_frame, col_name)
                    print("Minimum: ", col_minimum)
                except:
                    print("Minimum: Not applicable")
                try:
                    col_maximum = maximum(data_frame, col_name)
                    print("Maximum: ", col_maximum)
                except:
                    print("Maximum: Not applicable")
                try:
                    col_median = find_median(data_frame, col_name)
                    print("Median: ", col_median)
                except:
                    print("Median: Not applicable")
                try:
                    mode = find_mode(data_frame, col_name)
                    print("Mode: ", mode)
                except:
                    print("Mode: Could not process input")
                end_time = time.time()
                load_time = end_time - start_time

                print(
                    f"Stats printed successfully! time to process is {load_time:.3f} sec.")

            if (select_2 == "24"):
                print('(24) Search Element in Column: \n******************')
                print(formatted_time, 'Select column number to perform a search:')
                colnum = 0
                cols = []

                for i, column in enumerate(data_frame.columns):
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
                try:
                    print(formatted_time, 'Select column number to perform a search:')
                    colnum = 0
                    cols = []

                    for i, column in enumerate(data_frame.columns):
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
                    print(formatted_time, "Do you want to sort in Acending or Decending order?")
                    print(formatted_time, "Type A or D.")
                    sort_input = input("")
                    if(sort_input == "A"):
                        data_frame.sort_values([data_frame.columns[selectCol-1]],axis=0,ascending=[True],inplace = True)
                        print(data_frame[data_frame.columns[selectCol-1]])
                    if(sort_input == "D"):
                        data_frame.sort_values([data_frame.columns[selectCol-1]],axis=0,ascending=[False],inplace=True)
                        print(data_frame[data_frame.columns[selectCol-1]])
                except Exception as err25:
                    print(f"{type(err25)}: {err25}")


            if (select_2 == "26"):
                displayinput = int(input("Do you want to display [100], [1000], or [5000] rows of the dataset?\n"))
                try:
                    if (displayinput == 100 or displayinput == 1000 or displayinput == 5000):
                        print("Printing your request.\n")
                        print(data_frame.head(displayinput))
                    else:
                        print("invalid input. Try again.")
                except Exception as exc:
                    print("File has not loaded")

            if (select_2 == "27"):
                # Make it when the user selecet 27, it goes back to main
                print('(27)Back to Main Menu: \n******************')
                


        elif (select == "3"):  # Data analysis called here
            unique_crimes = ""
            most_crimes  = ""
            count_crimes = ""
            street_crimes = ""
            hollywood_crimes = ""
            common_crimes = ""
            dangerous_areas = ""
            gender_victim_analysis = ""

            
            print('Beginning Data Analysis: \n***************************')
            try:
                data_frame['DATE OCC'] = pd.to_datetime(data_frame['DATE OCC'])
                unique_crimes = data_frame['DATE OCC'].dt.year.value_counts().sort_index(ascending=False)
                print(formatted_time,
                        f'Show the total unique count of crimes per year sorted in descending order: ')
                print(unique_crimes,"\n")

                print(formatted_time, f'Top 5 areas with Most Crime events in all years(sorted by year and number of crime events)')
                most_crimes = data_frame['AREA NAME'].value_counts().head(5)
                print(most_crimes,"\n")

                data_frame['Date Rptd'] = pd.to_datetime(data_frame['Date Rptd'],format = formatted_time2)
                print(formatted_time, f'All months and unique count of crimes sorted in increasing order')
                count_crimes = data_frame.groupby(data_frame['Date Rptd'].dt.to_period("M")).size()
                print(count_crimes.sort_values(ascending=True),"\n")

              
                print(formatted_time, f'Top 10 streets with most crimes in LA in 2019 & total crimes in each street')#unfinished
                top_streets = data_frame.groupby('LOCATION').size().reset_index(name = 'Crime Count')
                street_crimes = top_streets.head(10).sort_values('Crime Count', ascending=False)
                print(street_crimes,"\n") 

                
                print(formatted_time, f'Top 5 most dangerous hours in Hollywood (and crimes per hour)\n')
                print("Times are listed in military time.")
                hollywood_crimes = data_frame[data_frame['AREA NAME'] == 'Hollywood']
                hourly_crimes = hollywood_crimes.groupby(hollywood_crimes['TIME OCC'].apply(lambda x: int(str(x).zfill(4)[:2]))).size().sort_values(ascending=False)
                dangerous_hours = hourly_crimes.head(5)

                # Convert output to string and remove the dtype line
                dangerous_hours_str = '\n'.join([line for line in str(dangerous_hours).split('\n') if 'dtype' not in line])
                print(dangerous_hours_str, "\n")

                pd.set_option('display.max_rows', 10)
                pd.set_option('display.max_columns', 10)
                pd.set_option('display.width', 1000)
                pd.options.display.float_format = "{:.2f}".format

                print(f'{formatted_time}: Details of the crimes that took the longest time to be reported\n')

                # Calculate the time difference between the 'DATE OCC' and 'Date Rptd' columns
                data_frame['Report Time Difference'] = (data_frame['Date Rptd'] - data_frame['DATE OCC']).dt.days

                # Find the maximum time difference
                max_time_diff = data_frame['Report Time Difference'].max()

                # Get the details of all crimes with the longest time to be reported
                longest_reported_crimes = data_frame[data_frame['Report Time Difference'] == max_time_diff]

                # Print the DataFrame in a more readable format
                print(longest_reported_crimes)

                # Drop the 'Report Time Difference' column
                data_frame.drop('Report Time Difference', axis=1, inplace=True)
               
                

                
                print(formatted_time, f'Top 10 most common crime types of all years')
                top10 = data_frame.groupby('Crm Cd Desc').size().sort_values(ascending=False)
                common_crimes = top10.head(10)
                print(common_crimes,"\n")

                
                print(formatted_time, f'Are women or men more likely to be a victim in LA between 11:00am to 1:00pm?')
                time_filtered_data = data_frame[(data_frame['TIME OCC'].apply(lambda x: int(str(x).zfill(4)[:2])) >= 11) & (data_frame['TIME OCC'].apply(lambda x: int(str(x).zfill(4)[:2])) < 13)]

                # Count the number of male and female victims
                male_victims = time_filtered_data[time_filtered_data['Vict Sex'] == 'M'].shape[0]
                female_victims = time_filtered_data[time_filtered_data['Vict Sex'] == 'F'].shape[0]

                # Compare the number of male and female victims
                if male_victims > female_victims:
                    gender_victim_analysis = "Men are more likely to be a victim in LA between 11:00am and 1:00pm."
                elif male_victims < female_victims:
                    gender_victim_analysis = "Women are more likely to be a victim in LA between 11:00am and 1:00pm."
                else:
                    gender_victim_analysis = "Men and women are equally likely to be a victim in LA between 11:00am and 1:00pm."
                
                print(gender_victim_analysis, "\n")
                
                # Month with most credit card frauds in 2019
                print(formatted_time,
                      f'Month with most credit card frauds in LA in 2019: ')
                df = pd.read_csv(selectedfile)
                df['Date Rptd'] = df['Date Rptd'].str.extract(
                    r'(\d+\/\d+\/\d+)', expand=False)
                df['DATE OCC'] = df['DATE OCC'].str.extract(
                    r'(\d+)', expand=False)
                months = ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]

                df.columns = [column.replace(" ", "_")
                              for column in df.columns]
                most_fraud = df.query(
                    'Crm_Cd_Desc == "CREDIT CARDS, FRAUD USE ($950 & UNDER" and year == 2019')
                fraudz = most_fraud.groupby(['DATE_OCC'])[
                    'DATE_OCC'].count().reset_index(name="count")
                fraudz = fraudz.sort_values(by="count", ascending=False)
                arr = fraudz['DATE_OCC'].tolist()
                index = int(arr[0]) - 1
                highest_fraud = months[index]
                print(highest_fraud, "\n")
                
                #Most dangerous areas for men 65 or older
                print(formatted_time, f'Top 5 most dangerous areas for older men (age from 65+) in december of 2018.')
                df = pd.read_csv(selectedfile)
                df.columns = [column.replace(" ", "_")
                              for column in df.columns]
                df['Date_Rptd'] = df['Date_Rptd'].str.extract(
                    r'(\d+)', expand=False)

                oldies = df.query(
                    'Vict_Age >= 65 and year == 2018 and Vict_Sex == "M" and Date_Rptd == "12"')
                oldies = oldies.groupby(['AREA_NAME'])[
                    'AREA_NAME'].count().reset_index(name="count")
                oldies = oldies.sort_values(by="count", ascending=False)
                arr = oldies['AREA_NAME'].tolist()
                i = 0
                while i < 5:
                    print(arr[i])
                    i = i + 1
          
              
                print("\nData Analysis Complete. Returning to Main Menu...")
               
            except Exception as error3:
                print(f"{type(error3)}: {error3}")
               



        elif (select == "4"):
            try:
                print("Printing the data_frame. (This may takes a long time)")
                print(data_frame.head)
            except Exception as er:
                print("File has not loaded.")

        elif (select == "5"):
            exit(0)
       
        print("\n-Input another valid command-")
        select = input(
            "(1) Load Data\n(2) Exploring Data\n(3) Data Analysis\n(4) Print Data Set\n(5) Quit\n")
    except Exception as err:
        print(f"{type(err)}: {err}")
    except KeyboardInterrupt:
        #if user needs ctrl-c, program will just go back to menu
        print("\nData proccesing took too long. Redirecting to previous menu...")
