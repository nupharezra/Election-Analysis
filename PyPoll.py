#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Asign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Declaring new list
candidate_options = []

#Declaring the empty dictionary
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]

        #if candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #begin tracking that candidates vote count (candidate votes is the dict[candidate name is the key] and setting each key = 0)
            candidate_votes[candidate_name] = 0

        #counting votes for each candidate
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping though the counts
#iterate through the candidate list
for candidate_name in candidate_votes:

        #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
    votes_percentage = float(votes) / float(total_votes) * 100

    #determine winning vote count and candidate
    #Determine if the votes are greater than the winning count
    if (votes > winning_count) and (votes_percentage > winning_percentage):

        #if true, then set winning count = votes and winning percentage = voter percentage
        winning_count = votes 
        winning_percentage = votes_percentage

        #set the winning candidate = to the candidates name
        winning_candidate = candidate_name
        
    #print out the winning candidate, vote count, and percentage to terminal
    print(f"{candidate_name}: recieved {votes_percentage:.1f}% ({votes:,})\n")
    
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n")
print(winning_candidate_summary)
    


