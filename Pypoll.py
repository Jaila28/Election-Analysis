import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Candidate Options
candidate_options = []

#Decalre the empty dictionary
candidate_votes = {}

#Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print each row in the CSV file
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any exisiting candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        #Putting this within the if statement will only render us 1 in the dictionary
        candidate_votes[candidate_name] += 1
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)

    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
        #Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        #To do: print out the winning candidate, vote count and percentage to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        txt_file.write(candidate_results)

    #Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)