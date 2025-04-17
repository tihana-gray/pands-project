# Iris Dataset Analysis

# First stage of the project: Data Analysis
# Importing necessary libraries

import os                           # Used to check file paths
import numpy as np                  # Used for calculating means and standard deviations

# 📚 References:
# - os: https://docs.python.org/3/library/os.html
# - numpy: https://numpy.org/doc/stable/

filename = "iris_data"
output_file = "summary.txt"

filename = "iris_data"    # Path to the raw data file
output_file = "variable_summary.txt"

# Each list holds one column of numeric data from the dataset
sepal_lengths = []     
sepal_widths = []      
petal_lengths = []     
petal_widths = []      

# 📚 Reference: Python lists – https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

# Reading the data from the file

if os.path.exists(filename):  # Checking if file exists before opening it

    with open(filename, 'r') as file:  # Opens the file for reading
        for line in file:
            line = line.strip()  # Removes newline and whitespace - CHECK THIS!!!!

            if line:  # Skip blank lines
                parts = line.split(',')  # Splitting each line by commas for better readability
                if len(parts) == 5:  # Making sure line has 5 values

                    # Converting string values to floats and append to lists
                    sepal_lengths.append(float(parts[0])) 
                    sepal_widths.append(float(parts[1]))
                    petal_lengths.append(float(parts[2]))
                    petal_widths.append(float(parts[3]))

# 📚 References:
# - open(): https://docs.python.org/3/library/functions.html#open, https://www.w3schools.com/Python/ref_func_open.asp
# - split(): https://docs.python.org/3/library/stdtypes.html#str.split
# - float(): https://docs.python.org/3/library/functions.html#float, https://www.w3schools.com/python/ref_func_float.asp
# - line.strip(): https://docs.python.org/3/library/stdtypes.html#str.strip, https://www.w3schools.com/python/ref_string_strip.asp
# - append(): https://docs.python.org/3/tutorial/datastructures.html#more-on-lists, https://www.w3schools.com/python/ref_list_append.asp,
# https://www.geeksforgeeks.org/python-list-append-method/