import os
import csv

# create election results header
print("                  ")
print("Election Results")
print("------------------")

# csv path
csvpath = 'Resources/election_data.csv'

# establish total votes
csvreader = open('Resources/election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    countofvotes = len(list(csvreader))
    print(f'Total Votes: {countofvotes}')

# establish candidates
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    allcandidates = []
    for row in csvreader:
        allcandidates.append(row[2])
    noduplicates = list(dict.fromkeys(allcandidates))

# establish vote count
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)
    khancount = allcandidates.count('Khan')
    correycount = allcandidates.count('Correy')
    licount = allcandidates.count('Li')
    otooleycount = allcandidates.count("O'Tooley")

# establish vote percentages
    khanpercentage = (khancount / countofvotes * 100)
    formattedkhan = "{:.3f}".format(khanpercentage)
    correypercentage = (correycount / countofvotes * 100)
    formattedcorrey = "{:.3f}".format(correypercentage)
    lipercentage = (licount / countofvotes * 100)
    formattedli = "{:.3f}".format(lipercentage)
    otooleypercentage = (otooleycount / countofvotes * 100)
    formattedotooley = "{:.3f}".format(otooleypercentage)

# establish winner
    winner = max(set(allcandidates), key = allcandidates.count)

# finish up results table
    print('------------------')
    print(f'{noduplicates[0]}: {formattedkhan}% ({khancount})')
    print(f'{noduplicates[1]}: {formattedcorrey}% ({correycount})')
    print(f'{noduplicates[2]}: {formattedli}% ({licount})')
    print(f'{noduplicates[3]}: {formattedotooley}% ({otooleycount})')
    print('------------------')
    print(f'Winner: {winner}')
    print('------------------')

with open(f'analysis/analysis.txt', 'w') as textfile:
    textfile.write("                  \n")
    textfile.write("Election Results\n")
    textfile.write("------------------\n")
    textfile.write(f"Total Votes: {countofvotes}\n")
    textfile.write('------------------\n')
    textfile.write(f'{noduplicates[0]}: {formattedkhan}% ({khancount})\n')
    textfile.write(f'{noduplicates[1]}: {formattedcorrey}% ({correycount})\n')
    textfile.write(f'{noduplicates[2]}: {formattedli}% ({licount})\n')
    textfile.write(f'{noduplicates[3]}: {formattedotooley}% ({otooleycount})\n')
    textfile.write('------------------\n')
    textfile.write(f'Winner: {winner}\n')
    textfile.write('------------------\n')