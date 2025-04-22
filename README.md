# Programming and Scripting Project

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

📚 References:
- https://archive.ics.uci.edu/dataset/53/iris
- https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html
- https://www.kaggle.com/datasets/uciml/iris
- https://www.geeksforgeeks.org/iris-dataset/

---

## 🧮 Part 2: Generating Summary

In the second part of this project I focused on getting summary statistics for each of the four numeric measurements in the Iris dataset:

Sepal length
Sepal width
Petal length
Petal width

The goal was to understand the general shape of the data and prepare me for the next part where I output and categorise data per variable.

1. *Reading the dataset*

I created lists for each dataset. The function `open()` opens the file and reads it line by line. For each line:\
Extra spaces and newlines are removed using `.strip()`
The values are split into separate pieces using `.split(',')`
The four numeric values are converted to floats and added to separate lists (one for each measurement).

According to my research, by using this approach I can work with strings, create loops and `if` statements and grow lists (by using `.append()`). 

📚 References (full list of refrences provided with the code):
- https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- https://www.w3schools.com/python/python_file_open.asp
- https://docs.python.org/3/library/stdtypes.html#str.strip
- https://docs.python.org/3/library/stdtypes.html#str.split
- https://docs.python.org/3/library/functions.html#float
- https://www.w3schools.com/python/ref_list_append.asp

2. *Creating DataFrame from the list*

After file reading, the script uses `pd.DataFrame()` to turn the lists into a table format. I also gave each row a name by using a list of names. 

📚 References (full list of refrences provided with the code):
- https://www.w3schools.com/python/pandas/pandas_dataframes.asp
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

3. *Calculations*

In the next step, by using `.describe().T`, the script calculates:
- Mean (average)
- Minimum and maximum
- Standard deviation
- Count (how many samples)

Because `.describe()` includes the median as the "50%", it was added again under the label "median" to make the output better to read.

📚 References (full list of refrences provided with the code):
- https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.T.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

My output so far:
![Output](<Part 1 output.png>)