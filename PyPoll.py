import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0

#initialize candidate list
candidate_option = []

#initialize candidate votes dictionary
candidate_votes = {}

#winning Candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with reader function
    file_reader = csv.reader(election_data)

    #print headers
    header = next(file_reader)
    

    # count each row in the csv file
    for row in file_reader:
        #add to vote count
        total_votes += 1
        #print cadidate names
        candidate_name = row [2]

        #add name to list if not already in list
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)

            #start counter for each candidate
            candidate_votes[candidate_name] = 0

        #add vote counts as loop through
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes)*100
        # update winning count, percent and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        Candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(Candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(Candidate_results)

    #print winning summary
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

        

   

   