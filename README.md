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
- https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

---

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

---

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

---------------------------------------------------------------------------------

1. *Reading the dataset*

I created lists for each dataset. The function `open()` opens the file and reads it line by line. For each line:\
- Extra spaces and newlines are removed using `.strip()`
- The values are split into separate pieces using `.split(',')`
- The four numeric values are converted to floats and added to separate lists (one for each measurement).

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


💭 *Personal Notes on this part:*

- I relied on online references abut also similar taskwork from Principles of Data Analytics module. Perhaps some of the solutions are not as pratical as they could be but it made me more comnfortable to use something that I used before.

