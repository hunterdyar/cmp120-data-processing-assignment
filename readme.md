## CMP Python Project 2

# Data Processing Assignment

You have been given 4 files:

1. py (boilerplate)
2. load\_data.py (provided, do not edit)
3. process\_strings.py (near empty placeholder)
4. a sample data file will be provided.

Main is the part of your program that will be run. Notice that it has the if \_\_name\_\_ == "\_\_main\_\_" magic line to check if it's being run directly or as a module.

- python main.py should execute your program

In main, import the 2 modules. The provided load\_data module and the process\_strings module that you will write for this assignment.

# Evaluation

When the code is evaluated, **a different data file** will be used, including more years of birth data in the same format. The "full" dataset contains over twice the number of lines.

The load\_data file will also be replaced with a "fresh" copy of the module. If you modify the load\_data file to get your code to work, it will not work when evaluated.

These two replacements are done to simulate how we work with code in the "real world", where we don't have control over input data, we have to use specific versions of modules, and so on.

- Your code will not be evaluated on performance/efficiency, within reason
- Your code will be evaluated on consistency

# About the data

Births\_00\_08.txt is basically a very simple spreadsheet. The data is from the US Social Security Administration. Every line contains the following, in order, separated by commas:

Year, Month, Day of Month, Day of week, Births

_In day of week, 1 is Monday and 7 is Sunday. process_strings.py includes an example function to turn the numbers into weekday strings for you._

**NOTE:** The data provided is technically a "csv" format. Python standard library has a CSV processing module ([https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)) which are **not allowed** to be used for this assignment.
This is because the assignment must be completed using knowledge we have covered so far in the course, and because the whole point is to do string parsing. There is also numpy, or the wonderful pandas ([https://pandas.pydata.org/](https://pandas.pydata.org/)) library that we will be using in the future. Using external modules is also not allowed for this assignment.

## About load\_data.py

Load\_data module provides functions for getting the contents of a file from the disk. It provides functions that return the data from the file in different formats.

_Note: In a real python project, the loading of the data and the parsing of the data would generally be done together, and the logic/processing/using/whatever happens separately. The point of this assignment is to do string parsing, so the load\_data file does less "work" than how one might organize their modules. A reasonable approach is "input,injesting,formatting", "Processing", and "output/prettifying" as separate types of problems/solutions, perhaps separate modules._

Function reference.

- *get\_data\_as\_blob* will return the entire data file as a single string.
- *get\_lines* will return the data file as an array of strings, with each entry an entire line.

## The Assignment

Add a comment with your name at the top of each of your files (main and process_strings)

Write functions that can do the following:

- When given a list of numbers, return the average
- Return the average number of births on any given day (month, day) of the year (average of all years).
- Return the average number of births on any given day of the week.
- Return the average number of births when given a specific month and day (average for all years)

When the program runs, it should use these functions to complete the following analysis:

('Report' here means 'print as complete sentence')

- What single day in the dataset had the fewest births?
- Report which day of the week contains the most births (as a complete sentence. IE: "Monday" not "1")
- How many fewer births happen on Dec. 25th than the average?
  - Compared to what? Average of all days? Average of other days in December? You decide what is meaningful.

The reports are just calculated outputs as full sentences. You don't need to then go "therefore...." or explain why. That is what the parson using this program will hypothetically do.

## Getting Started
When you get any individual line, you will want to use the split function to split it by commas.
You will then want to turn it into a tuple, casting the strings into appropriate types (...integers)

You could then make a new list of every item in the dataset as a tuple of integers, instead of a single string, and work with that.

There are many different ways to complete the challenge. For example, you could use the '.filter' function on arrays generously, or not use it at all.
