import os

import csv

csvpath = os.path.join("Resources", "election_data.csv")

voter_id, candidate, originalcandidates = [], [], []

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    print(csv_header)


    for row in csvreader:
        #create list with voter_id and candidate data
        voter_id.append(row[0])
        originalcandidates.append(row[2])
        #filtered original candidate list to filter the candidates
        if row[2] not in candidate:
            candidate.append(row[2])

#create dictionary to hold candidate(key) and the number of times they show up in the original list(values)
    name_dict = {} 
    for candidate in originalcandidates:
        if candidate not in name_dict:
            name_dict[candidate] = 1
        else:
            name_dict[candidate] += 1

#calculations
    for key, value in name_dict.items():
        print (f'{key} = {round(value/len(voter_id)*100,3)}% ({value})')

    print (f'Winner:  {max(name_dict, key = name_dict.get)}')

#create text file
file = open("pypollanalysis.txt", 'w+')

file.write(f'Election Results\n')

file.write(f'-----------------------------\n')

file.write(f'Total Votes:  {len(voter_id)}\n')

file.write(f'-----------------------------\n')

for key, value in name_dict.items():
        
    file.write(f'{key} = {round(value/len(voter_id)*100,3)}% ({value})\n')

file.write(f'-----------------------------\n')

file.write(f'Winner:  {max(name_dict, key = name_dict.get)}\n')

file.write(f'-----------------------------')




