# Programming and Scripting Project

----------------------------------------------------------------------------------------------------------------------

## 🌸 Part 1: About the Iris Dataset

The Iris dataset, introduced by British statistician Ronald A. Fisher in a 1936 research publication, stands as one of the most extensively utilised datasets within the domains of data science and machine learning.

This research titled *"The use of multiple measurements in taxonomic problems"* contains 150 samples (50 each) of iris flowers collected from there species:
- *Iris setosa*
- *Iris versicolor*
- *Iris virginica* 

Attribute information dataset is:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)
- Class

The primary objective of examining this dataset frequently involves determining the species of a flower utilising the provided measurements. Due to its limited size, clarity, and ease of measurement, this dataset has gained popularity as an introductory resource for acquiring skills in data analysis, data visualization, and classification techniques within the Python programming environment.\
It is commonly used in tutorials for learning Python libraries such as NumPy, Pandas, Matplotlib, and Scikit-learn. It’s also an excellent dataset to practice working with lists, loops, conditionals, and basic statistics.

**📚 References:**
- https://archive.ics.uci.edu/dataset/53/iris
- https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html
- https://www.kaggle.com/datasets/uciml/iris
- https://www.geeksforgeeks.org/iris-dataset/
- https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

----------------------------------------------------------------------------------------------------------------------

## 🔢 Part 2: Getting Data

I downloaded the Iris dataset from the official UCI Machine Learning Repository at: https://archive.ics.uci.edu/dataset/53/iris

I manually downloaded the iris.data file, along with the `iris.names` file (which contains summary descriptions of the columns and class labels), `iris.data` (which contains the full dataset with all 150 samples from the three species), `Index` file (showing the modification dates of the dataset) and `bezdekIris.data` (which also contains the full dataset with all 150 samples from the three species, named after one of the dataset researchers.)

**📚 References:**

- https://archive.ics.uci.edu/dataset/53/iris
- Bezdek, J., Keller, J., Krishnapuram, R., Kuncheva, L., & Pal, N. (1999). Will the real iris data please stand up? IEEE Transactions on Fuzzy Systems, 7(3), 368–369. https://doi.org/10.1109/91.771092 
https://lucykuncheva.co.uk/papers/jbjkrklknptfs99.pdf


After downloading the files, I created a folder in my project called iris_data. I placed all the downloaded files inside that folder. I keep the raw data separate from my Python scripts.

*The process of uploading to Git repository:*

- I used the following commands: 
`git add iris_data/`
`git commit -m "Added original Iris dataset files from UC Irvine`
`Source: https://archive.ics.uci.edu/dataset/53/iris"`

**📚 References:**

- https://graphite.dev/guides/how-to-push-code-from-vscode-to-github

----------------------------------------------------------------------------------------------------------------------

## 🔢 Part 3: Reading Data

In the next part of this project the goal is on getting summary statistics for each of the four numeric measurements in the Iris dataset:

- Sepal length
- Sepal width
- Petal length
- Petal width

I created a program called `analysis.py` which will be used for exploring the dataset.\
At the beginning of my script, I imported three libraries: `os`, `numpy`, and `pandas`.
- `os` is used to work with files and directories. This will be required for the later file handling and checking if a directory exists.
- `numpy` is a library that helps with numerical operations, which will also be required in the analysis part.
- `pandas` is used for working with data. It stores data dataframes, which are easier than managing lots of lists separately.

**📚 References:**

- https://docs.python.org/3/library/os.html
- https://numpy.org/doc/stable/
- https://pandas.pydata.org/docs/

----------

1. **Reading the dataset**

To start working with the Iris dataset, it's necessary to read the values from the file and organise them into something that Python can use for calculations.\ 
I created lists for each dataset. The plan was to go through the file line by line and split each row into separate values and then store it in the appropriate list.\
The function `open()` opens the file and reads it line by line. For each line:\
- I looped over each line in the file
- Extra spaces and newlines are removed using `.strip()`
- The values are split into separate pieces using `.split(',')`
- The four numeric values are converted to floats and added to separate lists (one for each measurement).

The first four values on each line are numeric, so I converted them from strings to floats using the `float()` function. 
Then, I used `.append()` to add each value to the correct list. These lists would later be used to create a DataFrame and calculate statistics like the mean, median, etc.

**📚 References (full list of refrences provided with the code):**
- https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- https://www.w3schools.com/python/python_file_open.asp
- https://docs.python.org/3/library/stdtypes.html#str.strip
- https://docs.python.org/3/library/stdtypes.html#str.split
- https://docs.python.org/3/library/functions.html#float
- https://www.w3schools.com/python/ref_list_append.asp

----------

2. **Creating DataFrame from the list**

After file reading, the script uses `pd.DataFrame()` to turn the lists into a table format. I also gave each row a name by using a list of names. Column names are `"sepal_length"`, `"sepal_width"`, `"petal_length"`, and `"petal_width"`.
Before creating the DataFrame, I included a check using `os.path.exists()` to see if the dataset file actually exists. If it doesn't, an `else` part is used to print a message with the filename and stop the program using `exit()`. This is helpful when debugging because the program won’t crash later from trying to read a missing file, and it lets me know exactly what went wrong.

**📚 References (full list of refrences provided with the code):**
- https://docs.python.org/3/library/os.path.html#os.path.exists
- https://www.w3schools.com/python/pandas/pandas_dataframes.asp
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- https://docs.python.org/3/library/sys.html#sys.exit

----------

3. **Calculations**

In this part, the script calculates summary statistics for each of the four numeric variables using the `.describe()` method in Pandas. This provides statistical measures such as count, mean, standard deviation, min, max, and percentiles (25%, 50%, and 75%). To make the output easier to read, `.T` is used to transpose the table so that each variable becomes a row and each statistical measure becomes a column.

Since `.describe()` does not label the median explicitly, the script uses Pandas `.median()` method to calculate and add a new column named `"median"` to the summary table. This step ensures the median is clearly identified and consistently formatted.

To keep the summary consistent, only the columns `"mean"`, `"min"`, `"max"`, `"std"`, and `"median"` are retained using the `.filter(items=[...])` method. This makes the filter applied to the labels of the index.

The rows are sorted alphabetically using `.sort_index()` and the table is printed to the terminal and saved to a file called `summary.txt` in tab-separated format using `.to_csv()`.

**📚 References (full list of refrences provided with the code):**
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html


## 💭 *Personal Notes on this part:*

- I relied on online references used for similar taskwork from Principles of Data Analytics module. Perhaps some of the solutions are not as pratical as they could be but it made me more comnfortable to use something that I used before (and explore it in more detail/repurpose it).
- My studying approach during this part and for text file/histogram part (and for previous module tasks) was to explore the code in the Notepad++ by using online references and examples and trying to replicate them to fit the task. Afterwards, I'd run the code in the VS Code and focus on errors, try different code versions and run the program again. However, this approach does not show detailed steps in GitHub so going forward I will save every step of the progress/testing in the repository.

----------------------------------------------------------------------------------------------------------------------

## 🔢 Part 4: Variable summaries to text files

In this section, the script generates individual text files for each of the four numeric variables in the Iris dataset: `sepal_length`, `sepal_width`, `petal_length`, and `petal_width`.

*The code performs the following steps:*

It first groups the variable names and their corresponding lists of values into a tuple of pairs. This makes the script to loop through each variable in a structured way.

Inside the loop, the following statistics are calculated with NumPy for each variable:
- Mean (average)
- Minimum and maximum
- Standard deviation (how spread out the values are)
- Median (middle value in the sorted list)

The script then uses `if-elif` conditions to match each variable name to a specific filename (e.g. `"sepal_length.txt"`) and opens that file in write mode (`"w"`).

Each statistic is written to the file using `f.write()`. Values are rounded to two decimal places for readability, and each statistic is labeled.

After writing, the file is closed using `f.close()` and then reopened in read mode `("r")` to print its contents to the terminal.

**📚 References (full list of refrences provided with the code):**
- https://www.w3schools.com/python/python_tuples.asp
- https://www.w3schools.com/python/python_for_loops.asp
- https://www.geeksforgeeks.org/numpy-mean-in-python/
- https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
- https://numpy.org/doc/stable/reference/generated/numpy.std.html
- https://www.geeksforgeeks.org/numpy-median-in-python/
- https://www.w3schools.com/python/ref_func_open.asp
- https://www.w3schools.com/python/python_conditions.asp
- https://www.w3schools.com/python/gloss_python_string_concatenation.asp
- https://www.w3schools.com/python/ref_func_round.asp
- https://stackoverflow.com/questions/60885439/how-the-n-symbol-works-in-python
- https://www.w3schools.com/python/ref_func_str.asp
- https://www.w3schools.com/python/ref_file_write.asp
- https://www.w3schools.com/python/ref_file_close.asp


## 💭 *Personal Notes on this part:*

- I decided to adjust the code, after speaking to some of the collegaues because the previous solution seemed prone to errors. There was a bit of an issue with figuring out how to reopen filles after writing and wheter to use `x` or `w` mode.
- Another issue was managing the structure and logic of the code when working with multiple related files.
- I also struggled arround `NameError` after I updated the name variable in one place and couldn't find where it was actually used and where it needs to be updated.

