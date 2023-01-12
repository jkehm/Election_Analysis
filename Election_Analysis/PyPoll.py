#Add our dependencies
import csv
import os

# Assign a variable to save a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Assign a variable for the file to load a path. 
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)



# Close File
    print(election_data)

