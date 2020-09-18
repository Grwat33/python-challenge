import os
import csv

# path = 'PyBank/Resources/budget_data.csv'
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    headers = next(csvreader)
    print(headers)
    for row in csvreader:
        print(row)
