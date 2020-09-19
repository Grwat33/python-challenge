import os
import csv

# create financial analysis header
print("                  ")
print("Financial Analysis")
print("------------------")

# csv path
csvpath = 'Resources/budget_data.csv'

# establish total months
csvreader = open('Resources/budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    countofmonths = len(list(csvreader))
    print(f'Total Months: {countofmonths}')

# establish total profit
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    nettotalprofit = []
    for row in csvreader:
        nettotalprofit.append(int(row[1]))
    print(f'Total Profit: ${sum(nettotalprofit)}')

# establish average of changes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    averagechange = []
    for row in csvreader:
        averagechange.append(int(row[1]))
    decimal = ((averagechange[85]-averagechange[0])/85)
    formatted = "{:.2f}".format(decimal)
    print(f'Average Change: ${formatted}') 

# establish greatest increase in profits
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    profits = []
    dates = []
    for row in csvreader:
        profits.append(row[1])
        dates.append(row[0])
    change = [int(profits[i + 1]) - int(profits[i]) for i in range(len(profits)-1)] 
    maxincreasechange = max(change)
    maxdecreasechange = min(change)
    increaseindex = change.index(maxincreasechange)
    decreaseindex = change.index(maxdecreasechange)
    print(f'Greatest Increase in Profits: {dates[increaseindex+1]} (${maxincreasechange})')
    print(f'Greatest Decrease in Profits: {dates[decreaseindex+1]} (${maxdecreasechange})')
