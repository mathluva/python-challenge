import os

import csv

import datetime

csvpath = os.path.join('Resources','budget_data.csv')
#create empty list variables to append data from row[0]-->months, row[1]--->profit_loss
months = []

profit_loss = []

change_profit_loss = []
#read in csv file budget_data.csv
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
#skip header row
    csv_header = next(csvreader) 

    print(f"CSV Header:  {csv_header}")
#append data in columns into the empty list from above
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
    print(f'Total Months: {len(months)}')
    print(f'Total: $ {sum(profit_loss)}')

#subtract 1 for header

    for i in range(len(profit_loss) -1):

    #loop through profit_loss list to create change in profit list
        change_profit_loss.append(int(profit_loss[i+1]-profit_loss[i])) 
        average_change = sum(change_profit_loss)/len(change_profit_loss)
        max_change_profit_value = max(change_profit_loss)
        min_change_loss_value = min(change_profit_loss)
    #find index for max/min profit loss
        max_change_profit_index = change_profit_loss.index(max(change_profit_loss)) +1 
        min_change_loss_index = change_profit_loss.index(min(change_profit_loss)) +1 

    print(f'Average Change:  ${round(average_change,2)}')
    print(f'Greatest Increase in Profits: {months[max_change_profit_index]} (${((max_change_profit_value))})')
    print(f'Greatest Decrease in Profits: {months[min_change_loss_index]} (${((min_change_loss_value))})')
    
#create text file pybankanalysis.txt
file = open("pybankanalysis.txt", "w+") 
#write in each row printed in text file, \n creates a new lline
file.write(f'Financial Analysis\n')

file.write(f'-----------------------------\n')

file.write(f'Total Months: {len(months)}\n')

file.write(f'Total: $ {sum(profit_loss)}\n')

file.write(f'Average Change:  ${round(average_change,2)}\n')

file.write(f'Greatest Increase in Profits: {months[max_change_profit_index]} (${(str(max_change_profit_value))})\n')
    
file.write(f'Greatest Decrease in Profits: {months[min_change_loss_index]} (${(str(min_change_loss_value))})\n')

file.close()

output_file = os.path.join("pybankanalysis.txt","r")
