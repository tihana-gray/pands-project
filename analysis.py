# Iris Dataset Analysis

# Author: Tihana Gray

# ------------------------------------------------------------------------
# First stage of the project: Data Analysis and Text File Outputs

# ------------------------------
# Importing necessary libraries
# ------------------------------

import os                           # Used to check if the data file exists at the specified path
import numpy as np                  # Used to calculate numerical statistics like mean and standard deviation
import pandas as pd                 # Used for data manipulation and analysis (DataFrames)

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

# Each list holds one column of numeric data from the dataset, they are empty now but will be filled with data later
# The lists are used to store the values for each variable (sepal length, sepal width, petal length, petal width)
# By creating separate lists it is easier to later calculate statistics for each variable
sepal_lengths = []     
sepal_widths = []      
petal_lengths = []     
petal_widths = []
species = []          # This list holds the species names (string values)      
# 📚 Reference: Python lists – https://docs.python.org/3/tutorial/datastructures.html#more-on-lists 
# https://www.w3schools.com/python/python_lists.asp


if os.path.exists(filename):  # Checking if file exists before opening it  → 📚 https://docs.python.org/3/library/os.path.html#os.path.exists

    with open(filename, 'r') as file:  # Opens the file for reading → 📚 https://www.w3schools.com/python/python_file_open.asp
        # if `with` is used then the file is automatically closed after the block is executed and doesn't leave the file open, which avoids memory leaks.

        for line in file: # this line starts a loop that reads each line of the file one by one
            # each line represents one row of the dataset  → 📚 https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

            line = line.strip()  # Removes newline charecters and whitespace and avoids errors with string processing
            # 📚 https://docs.python.org/3/library/stdtypes.html#str.strip

            if line:  # Skipping blank lines and empty rows → 📚 https://stackoverflow.com/questions/40647881/skipping-blank-lines-in-read-file-python/40647977
                parts = line.split(',')  # Splitting each line by commas for better readability → 📚 https://docs.python.org/3/library/stdtypes.html#str.split
                # each comma in the dataset separates values, so this creates a list of values for each line

                if len(parts) == 5:  # Making sure line has 5 values → 📚 https://realpython.com/len-python-function/
                    # This is done because the dataset has 5 columns: 4 numeric and 1 string (species)

                    # Converting string values to floats and append to lists
                    # Each line takes a string from the `parts` list and converts it to a float and appends it to the corresponding list
                    # The use of float() is important because the data is in string format and we need to convert it to a number for calculations
                    sepal_lengths.append(float(parts[0])) 
                    sepal_widths.append(float(parts[1]))
                    petal_lengths.append(float(parts[2]))
                    petal_widths.append(float(parts[3]))
                    species.append(parts[4]) # 5th value is the species name, for the scatterplot (this is a string)
                    # 📚 https://docs.python.org/3/library/functions.html#float
                    # 📚 https://www.w3schools.com/python/ref_list_append.asp


# 📚 Full list of references for this part are in the README.md file.


# -------------------------------
# Creating DataFrame
# -------------------------------

    df = pd.DataFrame({
        "sepal_length": sepal_lengths,
        "sepal_width": sepal_widths,
        "petal_length": petal_lengths,
        "petal_width": petal_widths,
        "species": species
    })
# This part creates Pandas DataFrame from the lists above (a table-like structure)
# Each list becomes a column in the DataFrame, with the column names being the keys in the dictionary
# Each value in the list becomes a row in that column
# 📚 Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

else: # This is part of an `if` statement that checks if the file exists
    print(f"File not found: {filename}") # uses an f-string to print a message that includes the value of the filename variable 
    # 📚 https://realpython.com/python-f-strings/
    exit() # 📚 https://docs.python.org/3/library/constants.html#exit
# This part runs if the file doesn't exist (the condition for `os.path.exists(filename)` failed).
# It prints an error message and exits the program.

# 📚 Full list of references for this part are in the README.md file.


# ----------------------------
# Calculating Summary Statistics Using Pandas
# ----------------------------

# Computing summary statistics for numerical columns only (excluding 'species')
# `.describe()` returns count, mean, std, min, 25%, 50%, 75%, max
# `.T` transposes the output so rows are variables and columns are stats (rows become columns and vice versa)
# Makes it easier to read, especially for large datasets - each variable is now a row
# `df` is the DataFrame created above
summary = df.describe().T # 📚 https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.T.html

# Adding the median separately (because `describe()` doesn't include median by default)
# `select_dtypes()` filters the DataFrame to include only numeric columns (so "species" is excluded)
summary["median"] = df.select_dtypes(include=['number']).median() # 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html

# Keeping only selected statistics that are needed for the summary.
# The `filter()` method is used to select specific rows (statistics) from the summary DataFrame
summary = summary.filter(items=["mean", "min", "max", "std", "median"])
# 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html

# Sorting rows alphabetically by feature name
# This is done to make it easier to read the summary
# The `sort_index()` method sorts the DataFrame by its index (which are the variable names)
summary = summary.sort_index()
# 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html

# Printing the summary to console
print(summary)

# Saving to text file (using tab as a separator)
# The `to_csv()` method is used to save the DataFrame to a text file
# The `sep='\t'` argument specifies that the values should be separated by tabs
summary.to_csv(output_file, sep='\t')
# 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html


# 📚 Full list of references for this part are in the README.md file.


# ------------------------------------------------------------
# Outputting a summary of each variable to a single text file
# ------------------------------------------------------------

# This tuple groups together the name of each variable with its list of values.
# Each item is a pair ("variable name", list_of_values)
# Tuples are useful when I want to keep related things together and loop through them.
iris_data = (
    ("sepal_length", sepal_lengths),
    ("sepal_width", sepal_widths),
    ("petal_length", petal_lengths),
    ("petal_width", petal_widths)
)
# 📚 Reference: https://www.w3schools.com/python/python_tuples.asp

# Looping through each variable one by one
for item in iris_data:
    name = item[0]       # The name of the variable, like "sepal_length"
    values = item[1]     # The actual list of float values for that variable
    # 📚 Reference: https://www.w3schools.com/python/python_for_loops.asp

    # Calculating statistics using NumPy and built-in functions
    # NumPy is used for numerical calculations, like mean and standard deviation
    # Built-in functions are used for min, max, and median
    mean_val = np.mean(values)      # average value → 📚 https://www.geeksforgeeks.org/numpy-mean-in-python/
    min_val = min(values)           # smallest value in the list → 📚 https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
    max_val = max(values)           # largest value in the list → 📚 https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
    std_val = np.std(values)        # standard deviation → 📚 https://numpy.org/doc/stable/reference/generated/numpy.std.html
    median_val = np.median(values)  # middle value → 📚 https://www.geeksforgeeks.org/numpy-median-in-python/

    # Using a fixed filename template based on the variable name → 📚 https://www.w3schools.com/python/ref_func_open.asp
    # This structure makes sure the output goes to the correct file
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
    # 📚 https://www.w3schools.com/python/python_conditions.asp
    
    # Writing each stat to the file. 
    f.write(name + " summary:\n")                         
    # Writing the variable name as a header (joining variable name with string (summary)) → 📚 https://www.w3schools.com/python/gloss_python_string_concatenation.asp
    f.write("Mean: " + str(round(mean_val, 2)) + "\n")    # Rounding numbers: 📚 https://www.w3schools.com/python/ref_func_round.asp
    f.write("Min: " + str(round(min_val, 2)) + "\n")      # Newline characters: 📚 https://stackoverflow.com/questions/60885439/how-the-n-symbol-works-in-python
    f.write("Max: " + str(round(max_val, 2)) + "\n")      # Converting values into strings: 📚 https://www.w3schools.com/python/ref_func_str.asp
    f.write("Std: " + str(round(std_val, 2)) + "\n")      # Adding text: 📚 https://www.w3schools.com/python/ref_file_write.asp
    f.write("Median: " + str(round(median_val, 2)) + "\n")

    f.close()  # Closing the file when done writing
    # 📚 https://www.w3schools.com/python/ref_file_close.asp

    # Re-opening the file in read mode to print the contents to the terminal
    # This is done to check if the file was written correctly
    # The file is opened in read mode ("r") to read the contents after writing
    # 📚 https://www.w3schools.com/python/python_conditions.asp
    if name == "sepal_length":
        f = open("sepal_length.txt", "r")
    elif name == "sepal_width":
        f = open("sepal_width.txt", "r")
    elif name == "petal_length":
        f = open("petal_length.txt", "r")
    elif name == "petal_width":
        f = open("petal_width.txt", "r")
    # 📚 https://www.w3schools.com/python/ref_func_open.asp
    print(f.read())                # This prints the contents of the file in the terminal
    f.close()                      # Closing it again after reading  


# 📚 Full list of references for this part are in the README.md file.


# ------------------------------------------------------------
## Second stage of the project: Histograms and Scatter Plots


# ------------------------------
# Histograms for each variable
# ------------------------------

import matplotlib.pyplot as plt   # Matplotlib used for basic plotting → 📚 https://matplotlib.org/stable/users/index.html
import seaborn as sns             # Seaborn used for plotting features and styling → 📚 https://seaborn.pydata.org/

# Looping through each variable from iris_data tuple
for item in iris_data:
    name = item[0]     # The name of the variable (like "sepal_length")
    values = item[1]   # The actual list of values for that variable
    # 📚 https://stackoverflow.com/questions/10867882/how-are-tuples-unpacked-in-for-loops

    # Creating the plot
    plt.figure(figsize=(8, 6))    # Creates a new figure → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    # figsize sets the size of the figure (width=8, height=6) 

    # Creating the histogram using Seaborn
    sns.histplot(values, bins=20, kde=False, color="skyblue", edgecolor="black")  
    # Seaborn histplot → 📚 https://seaborn.pydata.org/generated/seaborn.histplot.html
    # bins=20 makes 20 bars
    # kde=False removes the smooth curve (only bars) → 📚 https://www.geeksforgeeks.org/seaborn-distribution-plots/?ref=oin_asr2
    # color and edgecolor set the colour of the bars and their edges and improves visibility

    # Adding titles and axis labels
    plt.title(name + " Distribution", fontsize=14)    # Adding title → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
    plt.xlabel(name, fontsize=12)                     # X-axis label → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
    plt.ylabel("Frequency", fontsize=12)              # Y-axis label → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html

    plt.grid(True)  # Adding grid lines to the plot to make it easier to read → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
   
    # Saving the plot using a filename based on the variable name
    file_name = "histogram_" + name + ".png"     # Making the file name
    plt.savefig(file_name)                  # Saving the figure as a PNG file → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

    plt.close()   # Closing the figure to free up memory → 📚 https://www.geeksforgeeks.org/handling-memory-leaks-in-matplotlib/


# 📚 Full list of references for this part are in the README.md file.


# ------------------------------
# Scatter Plots for each pair of variables
# ------------------------------

# Importing necessary plotting libraries for visualisation
import matplotlib.pyplot as plt    # 📚 https://matplotlib.org/stable/users/index.html
import seaborn as sns             # 📚 https://seaborn.pydata.org/

# Example check — confirming df is defined → 📚 https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html
print(df.columns)
# This prints the column names of the DataFrame to confirm that it was created successfully

# ------------------------------
# First pair of variables: Sepal Length vs Petal Length

# Selecting two numerical variables from the DataFrame to compare
x_feature = "sepal_length"  # Will be plotted on the x-axis
y_feature = "petal_length"  # Will be plotted on the y-axis
# 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

# Creating the scatter plot → 📚 https://seaborn.pydata.org/generated/seaborn.scatterplot.html
plt.figure(figsize=(8, 6))  # Setting the size of the figure (width=8, height=6) → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
sns.scatterplot(
    x=df[x_feature],         # X axes: the x-values are taken from the column named in x_feature → 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    y=df[y_feature],         # Y axes: the y-values are taken from the column named in y_feature → 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    hue=df["species"],       # Adding colour by species → 📚 https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot
    palette="Spectral",      # Adding pallette → 📚 https://seaborn.pydata.org/tutorial/color_palettes.html
    s=80,                    # Size of each marker (dot) → 📚 https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot
    edgecolor="black",       # Adds a black border around each marker → 📚 same as above
    alpha=0.8                # Sets the transparency level of the dots (1.0 = opaque) → 📚 same as above
)

# Adding descriptive labels and a title → 📚 https://matplotlib.org/stable/api/pyplot_api.html
plt.xlabel("Sepal Length")           # Label for the x-axis → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
plt.ylabel("Petal Length")           # Label for the y-axis → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
plt.title("Sepal Length vs Petal Length")  # Title above the chart → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html

plt.grid(True)  # Adds grid lines to improve readability → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html

# Correlation → 📚 https://realpython.com/numpy-scipy-pandas-correlation-python/
corr = df[[x_feature, y_feature]].corr().iloc[0, 1]
# This calculates the correlation between the two selected features
# `df[[x_feature, y_feature]]` selects the two columns from the DataFrame
# `.corr()` calculates the correlation matrix for those two columns
# `.iloc[0, 1]` selects the correlation value between the two features
# 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
# 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html

# Subtitle → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html
plt.suptitle(f"Correlation: {corr:.2f}", fontsize=10, y=0.94, color='dimgray')

# Legend → 📚 https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
plt.legend(title="Species")

# Exporting the plot as a PNG file
# The file name is set to "sepal_vs_petal_length_scatterplot.png"
plt.savefig("scatterplot_sepal_length_vs_petal_length.png")  # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
plt.close()  # Close the figure after saving → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html


# ------------------------------
# Second pair of variables: Sepal Length vs Petal Width

# (this code and the following variables repeat the same process as above)
# Different pallete is used for variety
# Shows how petal width scales with sepal length

x_feature = "sepal_length"
y_feature = "petal_width"

plt.figure(figsize=(8, 6))

sns.scatterplot(
    x=df[x_feature],         
    y=df[y_feature],
    hue=df["species"],       
    palette="icefire",      
    s=80,                    
    edgecolor="black",       
    alpha=0.8                
)

plt.xlabel("Sepal Length")         
plt.ylabel("Petal Width")          
plt.title("Sepal Length vs Petal Width")

plt.grid(True)

corr = df[[x_feature, y_feature]].corr().iloc[0, 1]

plt.suptitle(f"Correlation: {corr:.2f}", fontsize=10, y=0.94, color='dimgray')

plt.legend(title="Species")

plt.savefig("scatterplot_sepal_length_vs_petal_width.png")

plt.close()


# ------------------------------
# Third pair of variables: Sepal Width vs Petal Length

# (this code and the following variables repeat the same process as above)
# Different pallete is used for variety 
# Shows how petal length scales with sepal width

x_feature = "sepal_width"
y_feature = "petal_length"

plt.figure(figsize=(8, 6))

sns.scatterplot(
    x=df[x_feature],         
    y=df[y_feature],         
    hue=df["species"],       
    palette="ch:s=-.2,r=.6", # Using a different palette for variety
    s=80,                    
    edgecolor="black",       
    alpha=0.8                
)

plt.xlabel("Sepal Width")          
plt.ylabel("Petal Length")         
plt.title("Sepal Width vs Petal Length") 

plt.grid(True)

corr = df[[x_feature, y_feature]].corr().iloc[0, 1]

plt.suptitle(f"Correlation: {corr:.2f}", fontsize=10, y=0.94, color='dimgray')

plt.legend(title="Species")

plt.savefig("scatterplot_sepal_width_vs_petal_length.png")

plt.close()


# ------------------------------
# Fourth pair of variables: Sepal Width vs Petal Width

# (this code and the following variables repeat the same process as above)
# Different pallete is used for variety
# Shows how petal width scales with sepal width

x_feature = "sepal_width"
y_feature = "petal_width"

plt.figure(figsize=(8, 6))

sns.scatterplot(
    x=df[x_feature],         
    y=df[y_feature],         
    hue=df["species"],       
    palette="Paired",      
    s=80,                    
    edgecolor="black",       
    alpha=0.8                
)

plt.xlabel("Sepal Width")          
plt.ylabel("Petal Width")          
plt.title("Sepal Width vs Petal Width")

plt.grid(True)

corr = df[[x_feature, y_feature]].corr().iloc[0, 1]

plt.suptitle(f"Correlation: {corr:.2f}", fontsize=10, y=0.94, color='dimgray')

plt.legend(title="Species")

plt.savefig("scatterplot_sepal_width_vs_petal_width.png")

plt.close()


# ------------------------------
# Fifth pair of variables: Petal Length vs Petal Width

# (this code and the following variable repeats the same process as above)
# Different pallete is used for variety
# Shows how petal width scales with petal length

x_feature = "petal_length"
y_feature = "petal_width"

plt.figure(figsize=(8, 6))

sns.scatterplot(
    x=df[x_feature],         
    y=df[y_feature],         
    hue=df["species"],       
    palette="magma",      
    s=80,                    
    edgecolor="black",       
    alpha=0.8                
)

plt.xlabel("Petal Length")         
plt.ylabel("Petal Width")          
plt.title("Petal Length vs Petal Width")

plt.grid(True)

corr = df[[x_feature, y_feature]].corr().iloc[0, 1]

plt.suptitle(f"Correlation: {corr:.2f}", fontsize=10, y=0.94, color='dimgray')

plt.legend(title="Species")

plt.savefig("scatterplot_petal_length_vs_petal_width.png")  
plt.close()


# ------------------------------
# Sixth pair of variables: Petal Length vs Sepal Width

# (this code repeats the same process as above)
# Different pallete is used for variety
# Shows how sepal width scales with petal length

x_feature = "petal_length"  
y_feature = "sepal_width"

plt.figure(figsize=(8, 6))

sns.scatterplot(
    x=df[x_feature],         
    y=df[y_feature],         
    hue=df["species"],       
    palette="coolwarm",      
    s=80,                    
    edgecolor="black",       
    alpha=0.8                
)

plt.xlabel("Petal Length")         
plt.ylabel("Sepal Width")          
plt.title("Petal Length vs Sepal Width")

plt.grid(True)

corr = df[[x_feature, y_feature]].corr().iloc[0, 1]

plt.suptitle(f"Correlation: {corr:.2f}", fontsize=10, y=0.94, color='dimgray')

plt.legend(title="Species")

plt.savefig("scatterplot_petal_length_vs_sepal_width.png")
plt.close()


# 📚 Full list of references for this part are in the README.md file.


# ------------------------------------------------------------
## Third stage of the project: Other Analysis and Visualisation

# ------------------------------
# Class Distribution
# ------------------------------

# matplotlib and seaborn are already imported above
# This part shows the distribution of species in the dataset

# ------------------------------
# Box plot for Petal Length

plt.figure(figsize=(8, 6))  # Setting figure width to 8 and height to 6 inches

sns.boxplot(x="species", y="petal_length", hue="species", data=df, palette="Set2")
  # Shows categorical variable on x-axis and numerical variable on y-axis
  # x="species" shows a separate box for each class of species
  # y="petal_length" shows the distribution of petal lengths for each species
  # Source DataFrame is df
  # Custom colour palette
# 📚 https://seaborn.pydata.org/generated/seaborn.boxplot.html

# Adding strip plot to show individual data points
# This adds underlying distributions on top of the box plot
sns.stripplot(x="species", y="petal_length", data=df, color="red", size=4, jitter=True, dodge=True, alpha=0.6)
# 📚 https://seaborn.pydata.org/generated/seaborn.stripplot.html

# Adding titles and labels
plt.xlabel("Species")                      # X-axis label → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
plt.ylabel("Petal Length (cm)")            # Y-axis label → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
plt.title("Class Distribution: Petal Length")  # Overall plot title → 📚 https://www.geeksforgeeks.org/matplotlib-pyplot-title-in-python/
plt.suptitle("Showing petal length variation across species", fontsize=10, color="dimgray")

plt.grid(True)  # Adding grid lines to the plot to make it easier to read → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html

plt.savefig("boxplot_class_distribution_petal_length.png")
plt.close()


# ------------------------------
# Box plot for Sepal Length

# (this code repeats the same process as above)
# Different pallete is used for variety

plt.figure(figsize=(8, 6))

sns.boxplot(x="species", y="sepal_length", hue="species", data=df, palette="rocket")

sns.stripplot(x="species", y="sepal_length", data=df, color="red", size=4, jitter=True, dodge=True, alpha=0.6)

plt.xlabel("Species")                    
plt.ylabel("Sepal Length (cm)")          
plt.title("Class Distribution: Sepal Length") 
plt.suptitle("Showing sepal length variation across species", fontsize=10, color="dimgray")

plt.grid(True)

plt.savefig("boxplot_class_distribution_sepal_length.png")
plt.close()


# ------------------------------
# Box plot for Sepal Width

# (this code repeats the same process as above)
# Different pallete is used for variety

plt.figure(figsize=(8, 6))

sns.boxplot(x="species", y="sepal_width", hue="species", data=df, palette="viridis")

sns.stripplot(x="species", y="sepal_width", data=df, color="red", size=4, jitter=True, dodge=True, alpha=0.6)

plt.xlabel("Species")                    
plt.ylabel("Sepal Width (cm)")          
plt.title("Class Distribution: Sepal Width") 
plt.suptitle("Showing sepal width variation across species", fontsize=10, color="dimgray")

plt.grid(True)

plt.savefig("boxplot_class_distribution_sepal_width.png")
plt.close()


# ------------------------------
# Box plot for Petal Width

# (this code repeats the same process as above)
# Different pallete is used for variety

plt.figure(figsize=(8, 6))

sns.boxplot(x="species", y="petal_width", hue="species", data=df, palette="cubehelix")

sns.stripplot(x="species", y="petal_width", data=df, color="red", size=4, jitter=True, dodge=True, alpha=0.6)

plt.xlabel("Species")                    
plt.ylabel("Petal Width (cm)")          
plt.title("Class Distribution: Petal Width") 
plt.suptitle("Showing petal width variation across species", fontsize=10, color="dimgray")

plt.grid(True)

plt.savefig("boxplot_class_distribution_petal_width.png")
plt.close()

# 📚 Full list of references for this part are in the README.md file.


# ------------------------------
# Feature Correlation Heatmap
# ------------------------------

# matplotlib and numpy are already imported above
# This part shows the correlation between features in the dataset

# Selecting only the numeric columns (excluding 'species', which is categorical) → 📚 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
correlation_matrix = df.select_dtypes(include='number').corr()
# The `.corr()` method calculates correlation coefficients between each pair of numeric features
# The result is a DataFrame showing how strongly features move together (1 = perfect positive, -1 = perfect negative)
# 📚 https://realpython.com/numpy-scipy-pandas-correlation-python/

plt.figure(figsize=(8, 6))  # Sets the figure size for the heatmap → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
# Using imshow to create the heatmap → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
plt.imshow(correlation_matrix, cmap='coolwarm')
# 'coolwarm' provides a diverging colour map (good for highlighting high and low values)
# 📚 https://matplotlib.org/stable/tutorials/colors/colormaps.html

plt.colorbar(label='Correlation Coefficient')  # Adds a colour scale legend → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html

tick_marks = np.arange(len(correlation_matrix.columns))  # 📚 https://numpy.org/doc/stable/reference/generated/numpy.arange.html
# This creates an array of tick marks for the x and y axes
# `correlation_matrix.columns` gets the names of the columns in the correlation matrix
# `len(correlation_matrix.columns)` gives the number of columns (and rows, since it's square)
# `np.arange()` creates an array of numbers from 0 to the number of columns

# Placing labels on X and Y axes → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
plt.xticks(tick_marks, correlation_matrix.columns)
plt.yticks(tick_marks, correlation_matrix.columns)
# This sets the tick marks on the x and y axes to the column names of the correlation matrix
# The `tick_marks` array is used to position the labels correctly

# Loop through the correlation matrix and printing value at each cell location
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        value = correlation_matrix.iloc[i, j]  # Get the correlation coefficient
        plt.text(j, i, f"{value:.2f}", ha='center', va='center', color='black')
        # 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
        # This adds the text to the heatmap at the correct position
        # `ha='center'` and `va='center'` center the text in the cell   
        # `color='black'` sets the text colour to black
        # `f"{value:.2f}"` formats the value to 2 decimal places
        # `correlation_matrix.iloc[i, j]` gets the value at row i and column j of the correlation matrix
        # `plt.text()` places the text at the specified coordinates (j, i) in the plot
        # `plt.text()` is used to add text annotations to the plot
        # `j` is the x-coordinate (column index) and `i` is the y-coordinate (row index)
        # The text is the correlation value formatted to 2 decimal places
        # `ha` and `va` specify the horizontal and vertical alignment of the text
        # `color` sets the text colour to black for better visibility
        # This loop goes through each cell in the correlation matrix and adds the correlation value as text in the heatmap

plt.title("Correlation Heatmap of Iris Features")  # Main plot title → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
plt.tight_layout()  # Automatically adjusts layout to prevent overlap → 📚 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html

# Exporting the final heatmap
plt.savefig("correlation_heatmap_of_iris_features.png")
plt.close()

# 📚 Full list of references for this part are in the README.md file.


## End of the analysis
# ------------------------------------------------------------

















