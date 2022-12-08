#### To Start
Use your virtual environment of choice or just the base python and install the required libraries
```
pip install -r requirements.txt
```

#### Running the program
```
python main.py -h
```

Required Arguments:
- (-u): user ID from the .Amber.license file associated with your license (lessly-peraton or the key tied to this ID)
- (-d): directory path relative to currect directory
- (-s): sensor ID
- (-t): threshold for NI classification (700)
- (-m): minimum number of rows required for classification (10)


#### Input file structure
The directory given should have all the separate files for the different maintenance events as csv.   
Each file naming convention is   
{"Open"/"Close"}-{Ship}\_{Engine}\_{MaintenanceEvent}.csv   
The first row is a header row so is removed.  
There should be 24 columns. The first six are removed because they are (not in any particular order):
- ship
- engine
- part
- maintenance event number
- timestamp
- open/closed  
Data processed then has 18 total columns

#### Breakdown of files
##### main.py\*
main file to run the program and parse arguments

##### amber_DPAS.py\*
has the amber functions and processes the data

##### color_class.py
codes for fancy printing text to the command line

##### print_functions.py
two functions to print the summary and the confusion matrix

##### requirements.txt
list of python libraries needed

##### \*important for edits

