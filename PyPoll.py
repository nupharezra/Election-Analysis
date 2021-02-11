#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Asign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

#to do: read and analyze the data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print ethe header row
    headers = next(file_reader)
    print(headers)
