import os
import csv

# Define the path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("analysis", "election_summary.txt")

# Total number of votes
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Has headers so use below to skip header
    next(csvfile)
    #Read through each row of data after the header
    row_count = sum(1 for row in csv_reader) 
    print(f'Total Votes: {row_count}')

# Complete list of candidates who received votes
# Starting empty list and initializing counters
candidate_list = []
charles_counter = 0
diane_counter = 0
raymon_counter = 0

with open(csvpath) as csvfile:
     csv_reader = list(csv.reader(csvfile, delimiter=","))
     #Skipping header by starting range at the first position
     for i in range(1, len(csv_reader)):
        if str(csv_reader[i][2]) == "Charles Casper Stockham":
            candidate_list.append("Charles Casper Stockham")
            charles_counter +=1
        elif str(csv_reader[i][2]) == "Diana DeGette":
            candidate_list.append("Diana DeGette")
            diane_counter +=1
        elif str(csv_reader[i][2]) == "Raymon Anthony Doane":
            candidate_list.append("Raymon Anthony Doane")
            raymon_counter +=1
        else: candidate_list.append("NA")


unique_candidates = list(set(candidate_list))

print(f'{unique_candidates[0]}: {round((charles_counter/row_count)*100,3)}% ({charles_counter})')
print(f'{unique_candidates[1]}: {round((diane_counter/row_count)*100,3)}% ({diane_counter})')
print(f'{unique_candidates[2]}: {round((raymon_counter/row_count)*100,3)}% ({raymon_counter})')

#Popular vote winner
if charles_counter > diane_counter and charles_counter > raymon_counter:
    print(f'Winner: {unique_candidates[0]}')
elif raymon_counter > diane_counter and raymon_counter > charles_counter:
    print(f'Winner: {unique_candidates[2]}')
else: print(f'Winner: {unique_candidates[1]}')



with open(outputfile, "w") as out_file:
    print("Election Results", file=out_file)
    print("-----------------------------", file=out_file)
    print(f'Total Votes: {row_count}', file=out_file)
    print("-----------------------------", file=out_file)
    print(f'{unique_candidates[0]}: {round((charles_counter/row_count)*100,3)}% ({charles_counter})', file=out_file)
    print(f'{unique_candidates[1]}: {round((diane_counter/row_count)*100,3)}% ({diane_counter})', file=out_file)
    print(f'{unique_candidates[2]}: {round((raymon_counter/row_count)*100,3)}% ({raymon_counter})', file=out_file)
    print("-----------------------------", file=out_file)
    if charles_counter > diane_counter and charles_counter > raymon_counter:
        print(f'Winner: {unique_candidates[0]}', file=out_file)
    elif raymon_counter > diane_counter and raymon_counter > charles_counter:
        print(f'Winner: {unique_candidates[2]}', file=out_file)
    else: print(f'Winner: {unique_candidates[1]}', file=out_file)