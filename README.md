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

## 🔢 Part 3: Importing necessary libraries

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

1. **Reading the data from the file**

To start working with the Iris dataset, it's necessary to read the values from the file and organise them into something that Python can use for calculations.\ 
I created lists for each dataset. The plan was to go through the file line by line and split each row into separate values and then store it in the appropriate list.\
The function `open()` opens the file and reads it line by line. For each line:\
- I looped over each line in the file
- Extra spaces and newlines are removed using `.strip()`
- The values are split into separate pieces using `.split(',')`
- The four numeric values are converted to floats and added to separate lists (one for each measurement).

The first four values on each line are numeric, so I converted them from strings to floats using the `float()` function. 
Then, I used `.append()` to add each value to the correct list. These lists would later be used to create a DataFrame and calculate statistics like the mean, median, etc.

**📚 References for this part:**

- https://www.w3schools.com/python/python_lists.asp
- https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- https://docs.python.org/3/library/os.path.html#os.path.exists
- https://docs.python.org/3/library/functions.html#open
- https://www.w3schools.com/Python/ref_func_open.asp
- https://www.w3schools.com/python/python_file_open.asp
- https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
- https://docs.python.org/3/library/stdtypes.html#str.strip
- https://www.w3schools.com/python/ref_string_strip.asp
- https://stackoverflow.com/questions/40647881/skipping-blank-lines-in-read-file-python/40647977
- https://docs.python.org/3/library/stdtypes.html#str.split
- https://www.geeksforgeeks.org/python-string-split/
- https://realpython.com/len-python-function/
- https://realpython.com/python-lists-tuples/#measuring-the-length-of-a-list
- https://docs.python.org/3/library/functions.html#float 
- https://www.w3schools.com/python/ref_func_float.asptypes.html#str.strip 
- https://docs.python.org/3/tutorial/datastructures.html#more-on-lists 
- https://www.w3schools.com/python/ref_list_append.asp
- https://www.geeksforgeeks.org/python-list-append-method

----------

2. **Creating DataFrame**

After file reading, the script uses `pd.DataFrame()` to turn the lists into a table format. I also gave each row a name by using a list of names. Column names are `"sepal_length"`, `"sepal_width"`, `"petal_length"`, and `"petal_width"`.
Before creating the DataFrame, I included a check using `os.path.exists()` to see if the dataset file actually exists. If it doesn't, an `else` part is used to print a message with the filename and stop the program using `exit()`. This is helpful when debugging because the program won’t crash later from trying to read a missing file, and it lets me know exactly what went wrong.

**📚 References for this part:**

- https://docs.python.org/3/library/os.path.html#os.path.exists
- https://www.w3schools.com/python/pandas/pandas_dataframes.asp
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- https://www.w3schools.com/python/ref_func_print.asp
- https://realpython.com/pandas-dataframe/
- https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
- https://realpython.com/python-f-strings/
- https://docs.python.org/3/library/constants.html#exit
- https://docs.python.org/3/library/sys.html#sys.exit

----------

3. **Calculating Summary Statistics Using Pandas**

In this part, the script calculates summary statistics for each of the four numeric variables using the `.describe()` method in Pandas. This provides statistical measures such as count, mean, standard deviation, min, max, and percentiles (25%, 50%, and 75%). To make the output easier to read, `.T` is used to transpose the table so that each variable becomes a row and each statistical measure becomes a column.

Since `.describe()` does not label the median explicitly, the script uses Pandas `.median()` method to calculate and add a new column named `"median"` to the summary table. This step ensures the median is clearly identified and consistently formatted.

To keep the summary consistent, only the columns `"mean"`, `"min"`, `"max"`, `"std"`, and `"median"` are retained using the `.filter(items=[...])` method. This makes the filter applied to the labels of the index.

The rows are sorted alphabetically using `.sort_index()` and the table is printed to the terminal and saved to a file called `summary.txt` in tab-separated format using `.to_csv()`.

**📚 References for this part:**

- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
- https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.T.html
- https://www.geeksforgeeks.org/pandas-dataframe-t-function-in-python/
- https://stackoverflow.com/questions/54734957/difference-between-transpose-and-t-in-pandas
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
- https://www.w3schools.com/python/pandas/ref_df_select_dtypes.asp
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html
- https://www.w3schools.com/python/ref_stat_median.asp#:~:text=median()%20method%20calculates%20the,in%20a%20set%20of%20data.
- https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html
- https://realpython.com/pandas-sort-python/
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
- https://www.geeksforgeeks.org/python-sep-parameter-print/
- https://stackoverflow.com/questions/22116482/what-does-print-sep-t-mean


## 💭 *Personal Learning Notes on this part:*

- I relied on online references used for similar taskwork from Principles of Data Analytics module. Perhaps some of the solutions are not as pratical as they could be but it made me more comnfortable to use something that I used before (and explore it in more detail/repurpose it).
- My studying approach during this part and for text file/histogram part (and for previous module tasks) was to explore the code in the Notepad++ by using online references and examples and trying to replicate them to fit the task. Afterwards, I'd run the code in the VS Code and focus on errors, try different code versions and run the program again. However, this approach does not show detailed steps in GitHub so going forward I will save every step of the progress/testing in the repository.

----------------------------------------------------------------------------------------------------------------------

## 🔢 Part 4: Outputting a summary of each variable to a single text file

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

**📚 References for this part:**

- https://www.w3schools.com/python/python_tuples.asp
- https://www.w3schools.com/python/python_for_loops.asp
- https://realpython.com/python-for-loop/
- https://www.geeksforgeeks.org/numpy-mean-in-python/
- https://www.geeksforgeeks.org/use-of-min-and-max-in-python/
- https://realpython.com/python-min-and-max/
- https://www.geeksforgeeks.org/numpy-std-in-python/
- https://numpy.org/doc/stable/reference/generated/numpy.std.html
- https://www.geeksforgeeks.org/numpy-median-in-python/
- https://www.w3schools.com/python/ref_func_open.asp
- https://www.w3schools.com/python/python_conditions.asp
- https://superuser.com/questions/940463/file-names-starting-with-a-string-in-the-format-of-txt-give-error-in-for
- https://www.w3schools.com/python/python_strings_methods.asp
- https://www.w3schools.com/python/gloss_python_string_concatenation.asp
- https://www.w3schools.com/python/ref_func_round.asp
- https://stackoverflow.com/questions/60885439/how-the-n-symbol-works-in-python
- https://www.geeksforgeeks.org/python-new-line-add-print-a-new-line/
- https://realpython.com/if-name-main-python/
- https://www.w3schools.com/python/ref_func_str.asp
- https://www.w3schools.com/python/ref_file_write.asp
- https://www.w3schools.com/python/ref_file_close.asp


## 💭 *Personal Learning Notes on this part:*

- I decided to adjust the code, after speaking to some of the collegaues because the previous solution seemed prone to errors. There was a bit of an issue with figuring out how to reopen filles after writing and wheter to use `x` or `w` mode.
- Another issue was managing the structure and logic of the code when working with multiple related files.
- I also struggled arround `NameError` after I updated the name variable in one place and couldn't find where it was actually used and where it needs to be updated.

----------------------------------------------------------------------------------------------------------------------

## 📊 Part 5: Histograms for Each Variable

This section creates a histogram for each of the four numerical variables in the Iris dataset using `Seaborn` and `Matplotlib`.

The variables are:
- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`

The script loops through each variable using a tuple that pairs variable names with their corresponding list of values. For each variable, a histogram is plotted using `sns.histplot()` with 20 bins and a clean color scheme (skyblue fill and black edge). Labels, titles, and grid lines are added using `matplotlib.pyplot` functions. The final figure is saved as a .png file named after the variable (e.g., `sepal_length_histogram.png`).

**📚 References for this part:**

- https://matplotlib.org/stable/users/index.html
- https://seaborn.pydata.org/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
- https://seaborn.pydata.org/generated/seaborn.histplot.html
- https://stackoverflow.com/questions/10867882/how-are-tuples-unpacked-in-for-loops
- https://www.geeksforgeeks.org/seaborn-distribution-plots/?ref=oin_asr2
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
- https://stackoverflow.com/questions/72057721/adding-a-black-edgecolor-around-to-legend-entries-in-matplotlib
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
- https://www.geeksforgeeks.org/handling-memory-leaks-in-matplotlib/


## 💭 *Personal Learning Notes on this part:*

During this part of the project, I went through several iterations of the code. I tried different approaches to plotting and made multiple versions with only slight changes between them. At one point, I mistakenly implemented scatterplots instead of histograms because I lost track of the task order. This led to some duplicated work and confusion about which method best matched the project requirements. It became obvious that planning before coding is important (especially when juggling another module project at the same time and things gets mixed up easily), keeping track of instructions, and distinguishing between similar project tasks.

----------------------------------------------------------------------------------------------------------------------

## 📊 Part 6: Scatter Plots for Each Pair of Variables

This section of the code created scatter plots for each unique pair of numerical variables in the Iris dataset. These plots visually present relationships between measurements and assess how they distinguish between species.

Pairs of variables are:
- Sepal Length vs Petal Length
- Sepal Length vs Petal Width
- Sepal Width vs Petal Length
- Sepal Width vs Petal Width
- Petal Length vs Petal Width
- Petal Length vs Sepal Width

Each scatter plot compares two variables and uses different color `seaborn` colour palettes to differentiate between the three species of iris flowers. This helps in identifying patterns, clusters, and potential correlations within the data.

Stages:
1. Importing necessary libraries - `Matplotlib` is used for plotting graphs and `Seaborn` helps to achieve better visualisation of data.
2. I created 6 scatter plots, one for each unique pair of the four numerical values. For each plot two features were assigned to `x_feature` and `y_feature`. `sns.scatterplot()` was used to generate the plot.
3. `Matplotlib` was used for adding labels and titles to the plot se we can clearly see what which axis represents.
4. Next part calculated correlation between 2 selected variable pairs - `.corr()` is used to present correlations between columns and `.iloc[0, 1]` tells Pandas to give me the value from the first row and second column, which is the actual correlation between the plotted variables.
5. Afterwards, the plot is saved as PNG file and closed.

**📚 References for this part:**

- https://matplotlib.org/stable/users/index.html
- https://seaborn.pydata.org/
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html
- https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- https://seaborn.pydata.org/generated/seaborn.scatterplot.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
- https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot
- https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
- https://seaborn.pydata.org/tutorial/color_palettes.html
- https://matplotlib.org/stable/api/pyplot_api.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
- https://www.geeksforgeeks.org/matplotlib-pyplot-title-in-python/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
- https://www.geeksforgeeks.org/grids-in-matplotlib/
- https://realpython.com/numpy-scipy-pandas-correlation-python/
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
- https://www.w3schools.com/python/pandas/ref_df_iloc.asp
- https://www.w3schools.com/python/matplotlib_grid.asp
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html
- https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
- https://www.geeksforgeeks.org/matplotlib-pyplot-savefig-in-python/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
- https://matplotlib.org/stable/gallery/color/named_colors.html


## 💭 *Personal Learning Notes on this part:*

 At earlier stage of the project I started working on scatter plots instead of histograms and then I tried using a nested loop that repeats over pairs of variable. The idea was to automate the plotting process by reducing code duplication. However, this method has limitations because I couldn't get the flexibility I needed for colour grouping by species or styling. That's why I decided to use the already tested version, done for 'Principles of Data Analytics' module. In this code version, I duplicated the same code structure for each pair of variables and had better control of what I'm doing regarding grouping by species, adding visual features, etc. 


 ----------------------------------------------------------------------------------------------------------------------

## 📊 Part 7: Other Analysis and Visualisation

1. **Box Plots: Class Distribution**

This part of the analysis presents how the four main numerical measurements (sepal length, sepal width, petal length, and petal width) are distributed across the three iris species. The goal was to visually compare the range and variation of each measurement grouped by class (species).

To achieve this, I used a combination of box plots and strip plots. Box plots are useful for summarising distributions and comparing characteristics of data between categories. Strip plots show individual data points layered over the box plot for clearer interpretation.

Each plot is generated using `Seaborn` and `Matplotlib` (already imported for the earlier task). I started by creating a new figure using `plt.figure(figsize=(8, 6))`, which provides consistency across all visualisations. I used `sns.boxplot()` to create a box plot, where the x-axis represents species and the y-axis represents one of the numerical features. The `hue="species"` ensures colour separation for each species, and the palette is customised for each box plot. `sns.stripplot()` is used to add individual observations to the plot. These red dots give a clearer picture of how data points are distributed within each category. The use of `jitter=True` helps spread overlapping points horizontally, and `alpha=0.6` makes them semi-transparent so that patterns are still visible beneath the box plot. I also added grid lined, subtitle and axis labels to improve readibility.

I repated this process for each of the four measurements.

**📚 References for this part:**

- https://www.geeksforgeeks.org/box-plot/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
- https://seaborn.pydata.org/generated/seaborn.countplot.html
- https://seaborn.pydata.org/generated/seaborn.boxplot.html
- https://www.geeksforgeeks.org/boxplot-using-seaborn-in-python/
- https://seaborn.pydata.org/tutorial/color_palettes.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.htm
- https://www.geeksforgeeks.org/matplotlib-pyplot-title-in-python/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
- https://www.geeksforgeeks.org/matplotlib-pyplot-savefig-in-python/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
- https://seaborn.pydata.org/generated/seaborn.stripplot.html
- https://www.geeksforgeeks.org/stripplot-using-seaborn-in-python/
- https://www.geeksforgeeks.org/how-to-make-boxplots-with-data-points-using-seaborn-in-python/
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html
- https://www.geeksforgeeks.org/matplotlib-pyplot-suptitle-function-in-python/


## 💭 *Personal Learning Notes on this part:*

At the beginning, I tried to experiment with `sns.countplot()` but that made my box plot layout distorted and I decided to remove that completely. Also, initially I only used box plots but then decided to add `sns.stripplot()` because it looks nicer to see clusters and it's something I haven't tried before.

----------------------------------------------------------------------------------------------------------------------

2. **Correlation Heatmap of Iris Features**

I used `.select_dtypes(include='number')` from pandas to isolate the numeric features and then applied the `.corr()` method to get the correlation coefficients. This resulted in a square matrix showing how strongly each pair of features are linearly related. For example, values close to 1 indicate strong positive correlation, and values near -1 represent strong negative correlation. This presents pairs of features that tend to increase or decrease together.

To visualise the matrix, I used `plt.figure()` and `plt.imshow()` to convert the matrix into a heatmap image. The colormap `"coolwarm"` was chosen because it visually distinguishes strong negative and strong positive correlations using contrasting colours. I also added a colour bar using `plt.colorbar()` as a legend for the correlation scale.

Tick marks were created for both axes using `np.arange()` and these tick were mapped to the feature names. Also, numeric values were added into each cell of the heatmap by using `for` loop that accessed each cell in the correlation matrix using `.iloc[i, j]`. The values were formatted to two decimal places using f-string formatting and `plt.text()` with centered alignment, and black text for good contrast against the heatmap colours.

The heatmap was also given a title by using `plt.title()` and I adjusted the layout using `plt.tight_layout()` to prevent label overlap. The heatmap was saved as an image file using `plt.savefig()`.

**📚 References for this part:**

- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
- https://realpython.com/numpy-scipy-pandas-correlation-python/
- https://www.geeksforgeeks.org/how-to-draw-2d-heatmap-using-matplotlib-in-python/
- https://stackoverflow.com/questions/33282368/plotting-a-2d-heatmap
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
- https://matplotlib.org/stable/users/explain/colors/colormaps.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html
- https://www.geeksforgeeks.org/numpy-arrange-in-python/
- https://www.w3schools.com/datascience/ds_stat_correlation_matrix.asp
- https://numpy.org/doc/stable/reference/generated/numpy.arange.html
- https://docs.python.org/3/library/functions.html#len
- https://stackoverflow.com/questions/29432629/plot-correlation-matrix-using-pandas
- https://stackoverflow.com/questions/18648626/for-loop-with-two-variables
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
- https://www.geeksforgeeks.org/add-text-inside-the-plot-in-matplotlib/
- https://stackoverflow.com/questions/29294983/how-to-calculate-correlation-between-all-columns-and-remove-highly-correlated-on
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html


## 💭 *Personal Learning Notes on this part:*

I thought correlation heatmap would be appropriate addition to the research because I used it before I like the way it shows the strength and direction of relationships between all numeric features in one concise visual. It gives a quick overview of which features are closely related and which ones are not, which can support or challenge patterns observed earlier in the project.

## End