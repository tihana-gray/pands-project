# Iris Dataset Analysis

# First stage of the project: Data Analysis and Text File Outputs

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
output_file = "summary.txt" # Output file for summary statistics

# -------------------------------
# Reading the data from the file
# -------------------------------

# Each list holds one column of numeric data from the dataset
# By creating separate lists it is easier to later calculate statistics for each variable
sepal_lengths = []     
sepal_widths = []      
petal_lengths = []     
petal_widths = []      
# 📚 Reference: Python lists – https://shorturl.at/4HNnR, https://shorturl.at/EWtiN


if os.path.exists(filename):  # Checking if file exists before opening it  → 📚 https://shorturl.at/37VkW

    with open(filename, 'r') as file:  # Opens the file for reading → 📚 https://shorturl.at/6RZ23
        # if `with` is used then the file is automatically closed after the block is executed and doesn't
        # leave the file open, which avoids memory leaks.
        for line in file: # this line starts a loop that reads each line of the file one by one
            # each line represents one row of the dataset  → 📚 https://shorturl.at/EGDkb
            line = line.strip()  # Removes newline charecters and whitespace and avoids errors with string processing
            # 📚 https://shorturl.at/mt38Q

            if line:  # Skipping blank lines and empty rows → 📚 https://shorturl.at/r8jQ6
                parts = line.split(',')  # Splitting each line by commas for better readability → 📚 https://shorturl.at/rGLK2
                # each comma in the dataset separates values, so this creates a list of values for each line
                if len(parts) == 5:  # Making sure line has 5 values → 📚 https://shorturl.at/FeTZ6
                    # This is done because the dataset has 5 columns: 4 numeric and 1 string (species)

                    # Converting string values to floats and append to lists
                    # Each line takes a string from the `parts` list and converts it to a float
                    # and appends it to the corresponding list
                    # The use of float() is important because the data is in string format
                    # and we need to convert it to a number for calculations
                    sepal_lengths.append(float(parts[0])) 
                    sepal_widths.append(float(parts[1]))
                    petal_lengths.append(float(parts[2]))
                    petal_widths.append(float(parts[3]))
                    # 📚 https://shorturl.at/2UfNJ

# 📚 Full references for this part:
# - lists: https://www.w3schools.com/python/python_lists.asp
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# os.path.exists(): https://docs.python.org/3/library/os.path.html#os.path.exists
# - open(): https://docs.python.org/3/library/functions.html#open
# https://www.w3schools.com/Python/ref_func_open.asp
# https://www.w3schools.com/python/python_file_open.asp
# - for line in file: https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
# - line.strip(): https://docs.python.org/3/library/stdtypes.html#str.strip
# https://www.w3schools.com/python/ref_string_strip.asp
# - if line: https://stackoverflow.com/questions/40647881/skipping-blank-lines-in-read-file-python/40647977
# - line.split(): https://docs.python.org/3/library/stdtypes.html#str.split
# https://www.geeksforgeeks.org/python-string-split/
# if len(parts): https://realpython.com/len-python-function/
# https://realpython.com/python-lists-tuples/#measuring-the-length-of-a-list
# - float(): https://docs.python.org/3/library/functions.html#float 
# https://www.w3schools.com/python/ref_func_float.asptypes.html#str.strip 
# - append(): https://docs.python.org/3/tutorial/datastructures.html#more-on-lists 
# https://www.w3schools.com/python/ref_list_append.asp
# https://www.geeksforgeeks.org/python-list-append-method


# -------------------------------
# Creating DataFrame
# -------------------------------

    df = pd.DataFrame({
        "sepal_length": sepal_lengths,
        "sepal_width": sepal_widths,
        "petal_length": petal_lengths,
        "petal_width": petal_widths
    })
# This part creates Pandas DataFrame from the lists above
# Each list becomes a column in the DataFrame, with the column names being the keys in the dictionary
# Each value in the list becomes a row in that column
# 📚 Reference: https://shorturl.at/HZwa7

else:
    print(f"File not found: {filename}") # fixed to make a variable for the filename {} → 📚 https://shorturl.at/ruLrt
    exit() # 📚 https://shorturl.at/MfjNr
# This part runs if the file doesn't exist (the condition for `os.path.exists(filename)` failed).
# It prints an error message and exits the program.

# 📚 Full references for this part:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
# https://www.w3schools.com/python/pandas/pandas_dataframes.asp
# https://www.w3schools.com/python/ref_func_print.asp
# https://realpython.com/pandas-dataframe/
# https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
# https://docs.python.org/3/library/constants.html#exit
# https://docs.python.org/3/library/sys.html#sys.exit


# ----------------------------
# Calculating Summary Statistics Using Pandas
# ----------------------------

# Computing summary statistics for numerical columns only (excluding 'species')
# `.describe()` returns count, mean, std, min, 25%, 50%, 75%, max
# `.T` transposes the output so rows are variables and columns are stats (rows become columns and vice versa)
# Makes it easier to read, especially for large datasets
summary = df.describe().T # 📚 https://shorturl.at/44ABW

# Adding the median separately (because `describe()` doesn't include median by default)
# `select_dtypes()` filters the DataFrame to include only numeric columns
summary["median"] = df.select_dtypes(include=['number']).median() # 📚 https://shorturl.at/HhouQ

# Keeping only selected statistics that are needed for the summary.
summary = summary.filter(items=["mean", "min", "max", "std", "median"])
# 📚 https://shorturl.at/lbo5h

# Sorting rows alphabetically by feature name
summary = summary.sort_index()
# 📚 https://shorturl.at/2DWPz

# Printing the summary to console
print(summary)

# Saving to text file
summary.to_csv(output_file, sep='\t')
# 📚 https://shorturl.at/a4BtT

# 📚 Full references for this part:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
# https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.T.html
# https://www.geeksforgeeks.org/pandas-dataframe-t-function-in-python/
# https://stackoverflow.com/questions/54734957/difference-between-transpose-and-t-in-pandas
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
# https://www.w3schools.com/python/pandas/ref_df_select_dtypes.asp
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html
# https://www.w3schools.com/python/ref_stat_median.asp#:~:text=median()%20method%20calculates%20the,in%20a%20set%20of%20data.
# https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html
# https://realpython.com/pandas-sort-python/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
# https://www.geeksforgeeks.org/python-sep-parameter-print/
# https://stackoverflow.com/questions/22116482/what-does-print-sep-t-mean


# ------------------------------------------------------------
# Outputting a summary of each variable to a single text file
# ------------------------------------------------------------

# This tuple groups together the name of each variable with its list of values.
# Each item is a pair: ("variable name", list_of_values)
# Tuples are useful when I want to keep related things together and loop through them.
# 📚 Reference: https://shorturl.at/jxSzv

iris_data = (
    ("sepal_length", sepal_lengths),
    ("sepal_width", sepal_widths),
    ("petal_length", petal_lengths),
    ("petal_width", petal_widths)
)

# Looping through each variable one by one
for item in iris_data:
    name = item[0]       # The name of the variable, like "sepal_length"
    values = item[1]     # The actual list of float values for that variable
    # 📚 Reference: https://shorturl.at/LFo0l

    # Calculating statistics using NumPy
    mean_val = np.mean(values)      # average value → 📚 https://shorturl.at/Mjww6
    min_val = min(values)           # smallest value in the list → 📚 https://shorturl.at/HVPi4
    max_val = max(values)           # largest value in the list → 📚 https://shorturl.at/HVPi4
    std_val = np.std(values)        # standard deviation → 📚 https://shorturl.at/FR0wI
    median_val = np.median(values)  # middle value → 📚 https://shorturl.at/wRvLd

    # Using a fixed filename template based on the variable name → 📚 https://shorturl.at/giP1G
    if name == "sepal_length":
        f = open("sepal_length.txt", "w")
    elif name == "sepal_width":
        f = open("sepal_width.txt", "w")
    elif name == "petal_length":
        f = open("petal_length.txt", "w")
    elif name == "petal_width":
        f = open("petal_width.txt", "w")
    # Each variable matches the correct filename. If the variable name is "sepal_length", it opens "sepal_length.txt" for writing.
    # Else if it's "sepal_width", it opens "sepal_width.txt", and so on.
    # This way avoids errors with file names and makes it easier to manage the output files (creating conditions for each file name).
    # 📚 https://shorturl.at/cSxLk
    
    # Writing each stat to the file. 
    f.write(name + " summary:\n")                         
    # Writing the variable name as a header (joining variable name with string (summary)) → 📚 https://shorturl.at/95OZd
    f.write("Mean: " + str(round(mean_val, 2)) + "\n")    # Rounding numbers: 📚 https://shorturl.at/GXj8q
    f.write("Min: " + str(round(min_val, 2)) + "\n")      # Newline characters: 📚 https://shorturl.at/uKg9V
    f.write("Max: " + str(round(max_val, 2)) + "\n")      # Converting values into strings: 📚 https://shorturl.at/bQb1p
    f.write("Std: " + str(round(std_val, 2)) + "\n")      # Adding text: 📚 https://shorturl.at/KUlpf
    f.write("Median: " + str(round(median_val, 2)) + "\n")

    f.close()  # Closing the file when done writing
    # 📚 https://shorturl.at/FXv7x

    # Re-opening the file in read mode to print the contents
    # This is done to check if the file was written correctly
    # The file is opened in read mode ("r") to read the contents after writing
    # 📚 https://shorturl.at/BJ5M0
    if name == "sepal_length":
        f = open("sepal_length.txt", "r")
    elif name == "sepal_width":
        f = open("sepal_width.txt", "r")
    elif name == "petal_length":
        f = open("petal_length.txt", "r")
    elif name == "petal_width":
        f = open("petal_width.txt", "r")
    # 📚 https://shorturl.at/g4Ccu
    print(f.read())                # This prints the contents of the file in the terminal
    f.close()                      # Closing it again after reading  

# 📚 Full references for this part:
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_for_loops.asp
# https://realpython.com/python-for-loop/
# https://www.geeksforgeeks.org/numpy-mean-in-python/
# https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
# https://www.geeksforgeeks.org/numpy-std-in-python/
# https://numpy.org/doc/stable/reference/generated/numpy.std.html
# https://www.geeksforgeeks.org/numpy-median-in-python/
# https://www.w3schools.com/python/ref_func_open.asp
# https://www.w3schools.com/python/python_conditions.asp
# https://superuser.com/questions/940463/file-names-starting-with-a-string-in-the-format-of-txt-give-error-in-for
# https://www.w3schools.com/python/python_strings_methods.asp
# https://stackoverflow.com/questions/60885439/how-the-n-symbol-works-in-python
# https://www.geeksforgeeks.org/python-new-line-add-print-a-new-line/
# https://www.w3schools.com/python/gloss_python_string_concatenation.asp
# https://www.w3schools.com/python/ref_func_round.asp
# https://www.w3schools.com/python/ref_func_str.asp
# https://realpython.com/if-name-main-python/
# https://www.w3schools.com/python/ref_file_write.asp
# https://www.w3schools.com/python/ref_file_close.asp


# ------------------------------------------------------------
## Second stage of the project: Histograms and Scatter Plots


# ------------------------------
# Importing necessary libraries
# ------------------------------

import matplotlib.pyplot as plt   # 📚 Matplotlib used for basic plotting → https://matplotlib.org/stable/users/index.html
import seaborn as sns             # 📚 Seaborn used for better-looking graphs → https://seaborn.pydata.org/

# Looping through each variable from iris_data tuple
for item in iris_data:
    name = item[0]     # The name of the variable (like "sepal_length")
    values = item[1]   # The actual list of values for that variable

    # ------------------------------
    # Creating the plot
    # ------------------------------

    plt.figure(figsize=(8, 6))    # 📚 Creates a new figure → https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    sns.histplot(values, bins=20, kde=False, color="skyblue", edgecolor="black")  
    # 📚 Seaborn histplot → https://seaborn.pydata.org/generated/seaborn.histplot.html
    # - bins=20 makes 20 bars
    # - kde=False removes the smooth curve (only bars)
    # - color and edgecolor make it nicer looking

    # ------------------------------
    # Adding titles and labels
    # ------------------------------

    plt.title(name + " Distribution", fontsize=14)    # 📚 Add title → https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
    plt.xlabel(name, fontsize=12)                     # 📚 X-axis label → https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
    plt.ylabel("Frequency", fontsize=12)              # 📚 Y-axis label → https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html

    plt.grid(True)  # 📚 Adding grid lines to the plot to make it easier to read → https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html

    # ------------------------------
    # Saving the plot
    # ------------------------------

    file_name = name + "_histogram.png"     # Make the file name
    plt.savefig(file_name)                  # 📚 Save the figure as a PNG file → https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

    plt.close()   # 📚 Closing the figure to free up memory → https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html

# 📚 Reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html


# ------------------------------
# Histograms for each pair of variables
# ------------------------------

# Defining variable_names from the tuple structure used earlier
variable_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

# Dictionary to hold the actual values for each variable
variable_data = {
    "sepal_length": sepal_lengths,
    "sepal_width": sepal_widths,
    "petal_length": petal_lengths,
    "petal_width": petal_widths
}
# 📚 Reference: https://www.w3schools.com/python/python_dictionaries.asp

# Loop through each variable to create histograms
for variable_name in variable_names:
    values = variable_data.get(variable_name)  # Using .get() to access values
    # 📚 https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/

    plt.figure(figsize=(8, 6))  # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

    # Creating the histogram
    sns.histplot(values, bins=20, kde=False, color="skyblue", edgecolor="black")  
    # 📚 https://seaborn.pydata.org/generated/seaborn.histplot.html

    plt.title(variable_name + " Distribution", fontsize=14)  # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
    plt.xlabel(variable_name, fontsize=12)  # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
    plt.ylabel("Frequency", fontsize=12)    # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html

    plt.grid(True)  # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html

    filename = variable_name + "_histogram.png"
    plt.savefig(filename)  # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

    plt.close()  # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html

        