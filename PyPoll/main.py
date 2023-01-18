import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

output_text = "output.txt"


total_votes = 0

charles_votes = 0
diana_votes = 0
raymon_votes = 0

all_candidates = []
candidate_name = []
vote_percent = []
total_each_can =[]
vote_tally = []


final_results = {}


with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1 # loops through the csv and counts each vote 

        # Determines each candidcates votes by going through each current vote per candidate and increasing the count
        if str(row[2]) == 'Charles Casper Stockham':
            charles_votes = charles_votes + 1
        if str(row[2]) == 'Diana DeGette':
            diana_votes = diana_votes + 1
        if str(row[2]) ==  'Raymon Anthony Doane':
            raymon_votes = raymon_votes + 1

    # Calculates percentage of votes won by each candidate
    Charles_percent = round((charles_votes/total_votes) * 100, 2)  
    diana_percent = round((diana_votes/total_votes) * 100, 2)
    raymon_percent = round((raymon_votes/total_votes) * 100, 2)

    # prints in terminal: total votes, total votes per candidate, percentage of votes per candidate
    print(f' Total Votes: {total_votes}')
    print(f'Total Number of Votes for Charles: {charles_votes}')
    print(f'Percentage of Votes for Charles: {Charles_percent}%')
    print(f'Total Number of Votes for Diana: {diana_votes}')
    print(f'Percentage of Votes for Diana: {diana_percent}%')
    print(f'Total Number of Votes for Raymon: {raymon_votes}')
    print(f'Percentage of Votes for Raymon: {raymon_percent}%')


    # determines winner of the election
    if (Charles_percent > diana_percent) and (Charles_percent >raymon_percent): # if Charles has greater votes than the others, set winner as Charles
        winner = 'Charles Casper Stockham'
        print('Winner : Charles Casper Stockham')
    elif (diana_percent > raymon_percent) and (diana_percent > Charles_percent): # if Diana has greater votes than the others, set winner as Diana
        winner = 'Diana DeGette'
        print('Winner : Diana DeGette')
    elif (raymon_percent > Charles_percent) and (raymon_percent > diana_percent): # if Raymon has greater votes than the others, set winner as Raymon
        winner = 'Raymon Anthony Doane'
        print('Winner : Raymon Anthony Doane')



# print results in output file
with open(output_text, "w") as csvfile: 
  final_results = (
    f"Election Results \n" 
    f"---------------- \n"
    f"Total Votes: {total_votes} \n"
    f"---------------- \n"
    f"Charles Casper Stockham: {Charles_percent} '('{charles_votes}')' \n"
    f"Diana DeGette: {diana_percent} '('{diana_votes}')' \n"
    f"Raymon Anthony Doane: {raymon_percent} '('{raymon_votes}')' \n"
    f"---------------- \n"
    f"Winner: {winner} \n"
    f"---------------- \n")

  print(final_results)

  csvfile.write(final_results)