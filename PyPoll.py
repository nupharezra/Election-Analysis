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
candidate_votes = {}

county_list = []
county_dict = {}

#track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county and county voter turnout.
largest_county = ""
winning_county_count = 0
winning_counting_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]

         #Extract the county name from each row.
        county_name = row[1]

        #if candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #begin tracking that candidates vote count (candidate votes is the dict[candidate name is the key] and setting each key = 0)
            candidate_votes[candidate_name] = 0

        #Adding a vote for each candidate's count
        candidate_votes[candidate_name] += 1
    # Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # Add the existing county to the list of counties.
            county_list.append(county_name)

            # Begin tracking the county's vote count.
            county_dict[county_name] = 0

        # Add a vote to that county's vote count.
        county_dict[county_name] += 1

#save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #print final vote count to terminal - election_analysis.txt
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")

    #Save the final vote count to the txt file.
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_dict:

        # 6b: Retrieve the county vote count.
        county_votes = county_dict.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(county_votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
             f"{county_name}: recieved {county_percentage:.1f}% ({county_votes:,})\n")

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_votes > winning_county_count) and (county_percentage > winning_counting_percentage):
            largest_county = county_name
            winning_county_count = county_votes
            winning_count_percentage = county_percentage

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"--------------------------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"--------------------------------------------\n")
    
    #Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)
  
    #Determine the percentage of votes for each candidate by looping though the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:

            #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

            #calculate the percentage of votes
        votes_percentage = float(votes) / float(total_votes) * 100

        #Determine vote count and percentage for each candidate
        candidate_results = (
            f"{candidate_name}: recieved {votes_percentage:.1f}% ({votes:,})\n")

        #print out each candidates vote count and percentage to the termina
        print(candidate_results)

        #Save the candidate results to our text file
        txt_file.write(candidate_results)

        #determine winning vote count and candidate
        #Determine if the votes are greater than the winning count
        if (votes > winning_count) and (votes_percentage > winning_percentage):

            #if true, then set winning count = votes and winning percentage = voter percentage
            winning_count = votes 
            winning_percentage = votes_percentage

            #set the winning candidate = to the candidates name
            winning_candidate = candidate_name

    #print winning candidates results
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)

    #Save the sinning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
   


