# Iris Dataset Analysis

# First stage of the project: Data Analysis

# ------------------------------
# Importing necessary libraries
# ------------------------------

import os                           # Used to check file paths
import numpy as np                  # Used for calculating means and standard deviations
import pandas as pd                 # Used for data manipulation and analysis

# 📚 References:
# - os: https://docs.python.org/3/library/os.html
# - numpy: https://numpy.org/doc/stable/
# - pandas: https://pandas.pydata.org/docs/


# Defining file paths and variables
filename = "iris_data/iris.data"    # Path to the raw data file
output_file = "variable_summary.txt" # Output file for summary statistics

# -------------------------------
# Reading the data from the file
# -------------------------------

# Each list holds one column of numeric data from the dataset
sepal_lengths = []     
sepal_widths = []      
petal_lengths = []     
petal_widths = []      

# 📚 Reference: Python lists – https://docs.python.org/3/tutorial/datastructures.html#more-on-lists



if os.path.exists(filename):  # Checking if file exists before opening it

    with open(filename, 'r') as file:  # Opens the file for reading → 📚 https://shorturl.at/6RZ23
        for line in file:
            line = line.strip()  # Removes newline and whitespace 
            # 📚 https://docs.python.org/3/library/stdtypes.html#str.strip

            if line:  # Skip blank lines
                parts = line.split(',')  # Splitting each line by commas for better readability → 📚 https://shorturl.at/rGLK2
                if len(parts) == 5:  # Making sure line has 5 values

                    # Converting string values to floats and append to lists
                    sepal_lengths.append(float(parts[0])) 
                    sepal_widths.append(float(parts[1]))
                    petal_lengths.append(float(parts[2]))
                    petal_widths.append(float(parts[3]))
                    # 📚 https://docs.python.org/3/library/functions.html#float

# 📚 References:
# - open(): https://docs.python.org/3/library/functions.html#open, https://www.w3schools.com/Python/ref_func_open.asp
# https://www.w3schools.com/python/python_file_open.asp
# - split(): https://docs.python.org/3/library/stdtypes.html#str.split
# - float(): https://docs.python.org/3/library/functions.html#float, https://www.w3schools.com/python/ref_func_float.asp
# - line.strip(): https://docs.python.org/3/library/stdtypes.html#str.strip, https://www.w3schools.com/python/ref_string_strip.asp
# - append(): https://docs.python.org/3/tutorial/datastructures.html#more-on-lists, https://www.w3schools.com/python/ref_list_append.asp,
# https://www.geeksforgeeks.org/python-list-append-method/


    df = pd.DataFrame({
        "sepal_length": sepal_lengths,
        "sepal_width": sepal_widths,
        "petal_length": petal_lengths,
        "petal_width": petal_widths
    })
# 📚 Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

else:
    print(f"File not found: {filename}") # fixed to make a variable for the filename {} → 📚 https://rebrand.ly/66fbdc
    exit() # 📚 https://rebrand.ly/84ba31


# ----------------------------
# Calculating Summary Statistics Using Pandas
# ----------------------------

# Computing summary statistics for numerical columns only (excluding 'species')
# `.describe()` returns count, mean, std, min, 25%, 50%, 75%, max
# `.T` transposes the output so rows are variables and columns are stats
summary = df.describe().T

# 📚 References:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
# https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.T.html

# Adding the median separately (because `describe()` doesn't include median)
# `select_dtypes()` helps isolate numerical columns only
summary["median"] = df.select_dtypes(include=['number']).median() # 📚 https://shorturl.at/TJzuT

# 📚 Reference:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html

# Filtering only the columns we care about: mean, min, max, std, median
summary = summary[["mean", "min", "max", "std", "median"]]

# Sorting rows alphabetically by feature name
summary = summary.sort_index()

# 📚 Reference:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html

# Printing the summary to console
print(summary)

# Saving to text file
summary.to_csv("summary.txt", sep='\t')

# 📚 Reference:
# - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
# - else: https://www.w3schools.com/python/python_conditions.asp, https://www.geeksforgeeks.org/python-if-else/
# - min()/max(): https://docs.python.org/3/library/functions.html#min, https://www.geeksforgeeks.org/max-min-python/,
# - https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
# - https://realpython.com/python-min-and-max/#:~:text=Python%20uses%20these%20code%20points,min()%20and%20max()%20.&text=To%20find%20the%20smallest%20or,code%20points%20of%20initial%20characters.
# - numpy.mean(): https://numpy.org/doc/2.2/reference/generated/numpy.mean.html, https://www.geeksforgeeks.org/numpy-mean-in-python/


# ------------------------------------------------------------
# Outputting a summary of each variable to a single text file
# ------------------------------------------------------------

# This tuple below groups together the name of each variable with its list of values.
# Each item is a pair: ("variable name", list_of_values)
# Tuples are useful when I want to keep related things together and loop through them.
# 📚 Reference: https://www.w3schools.com/python/python_tuples.asp

iris_data = (
    ("sepal_length", sepal_lengths),
    ("sepal_width", sepal_widths),
    ("petal_length", petal_lengths),
    ("petal_width", petal_widths)
)

# Looping through each variable one by one
for item in iris_data:
    name = item[0]       # The name of the variable, like "sepal_length"
    values = item[1]     # The actual list of numbers for that variable

    # Now I calculate some basic statistics using NumPy
    mean_val = np.mean(values)      # 📚 https://www.geeksforgeeks.org/numpy-mean-in-python/
    min_val = min(values)           # 📚 https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
    max_val = max(values)           # 📚 https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
    std_val = np.std(values)        # 📚 https://numpy.org/doc/stable/reference/generated/numpy.std.html
    median_val = np.median(values)  # 📚 https://www.geeksforgeeks.org/numpy-median-in-python/

    # Now making a file just for this variable (e.g. "sepal_length.txt") → 📚 https://shorturl.at/DhS7F
    file_name = name + ".txt"  # Just adding ".txt" to the name to create text file 

    # Open the file in write mode ("w" = create or overwrite the file)
    f = open(file_name, "w")  # 📚 https://www.w3schools.com/python/ref_func_open.asp

    # Writing each stat to the file. 
    f.write(name + " summary:\n")
    f.write("Mean: " + str(round(mean_val, 2)) + "\n")    # Rounding numbers: 📚 https://www.w3schools.com/python/ref_func_round.asp
    f.write("Min: " + str(round(min_val, 2)) + "\n")      # Newline characters: 📚 https://shorturl.at/uKg9V
    f.write("Max: " + str(round(max_val, 2)) + "\n")      # Converting values into strings: 📚 https://www.w3schools.com/python/ref_func_str.asp
    f.write("Std: " + str(round(std_val, 2)) + "\n")      # Adding text: 📚 https://www.w3schools.com/python/ref_file_write.asp
    f.write("Median: " + str(round(median_val, 2)) + "\n")

    f.close()  # Closing the file when done writing
    # 📚 File closing info: https://www.w3schools.com/python/ref_file_close.asp

    # Re-opening the file in read mode to check if the output worked (this part is optional)
    f = open(file_name, "r")       # "r" = read-only mode
    print(f.read())                # This prints the contents of the file in the terminal
    f.close()                      # Closing it again after reading

# 📚 References:
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_for_loops.asp
# https://realpython.com/python-for-loop/
# https://www.geeksforgeeks.org/numpy-mean-in-python/
# https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
# https://www.geeksforgeeks.org/numpy-std-in-python/
# https://numpy.org/doc/stable/reference/generated/numpy.std.html
# https://www.geeksforgeeks.org/numpy-median-in-python/
# https://superuser.com/questions/940463/file-names-starting-with-a-string-in-the-format-of-txt-give-error-in-for
# https://www.w3schools.com/python/ref_func_open.asp
# https://www.w3schools.com/python/python_strings_methods.asp
# https://stackoverflow.com/questions/60885439/how-the-n-symbol-works-in-python
# https://www.w3schools.com/python/ref_func_round.asp
# https://www.w3schools.com/python/ref_func_str.asp
# https://www.w3schools.com/python/ref_file_write.asp
# https://www.w3schools.com/python/ref_file_close.asp
