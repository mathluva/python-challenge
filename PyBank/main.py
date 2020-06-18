import os

import csv

import statistics

csvpath = os.path.join('Resources','budget_data.csv')

months = []

profit_loss = []

change_profit_loss = []

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader) #skip header row

    print(f"CSV Header:  {csv_header}")

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
    print(f'Total Months: {len(months)}')
    print(f'Total: $ {sum(profit_loss)}')

    for i in range(len(profit_loss) -1):
        change_profit_loss.append(int(profit_loss[i+1]-profit_loss[i]))
        average_change = sum(change_profit_loss)/len(change_profit_loss)
        #max_change_profit = max(change_profit_loss)
        #min_change_loss = min(change_profit_loss)
        max_change_profit = change_profit_loss.index(max(change_profit_loss)) +1
        min_change_loss = change_profit_loss.index(min(change_profit_loss)) +1
    print(str(max_change_profit))
    print(str(min_change_loss))
    print(f'Greatest Increase Profit: {months[max_change_profit]}(${(str(min_change_lowest))})')
    print(f'Average Change:  ${round(average_change,2)}')
    #print(max(average_change))
   
    #print(sum(change_profit_loss))
        #int(len(change_profit_loss)-1)
    #print(f'Average Change:  ${round(average_change, 2)}