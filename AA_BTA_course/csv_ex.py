import csv

with open('Downloads/samp.csv','r') as f:
    data =csv.reader(f)
    for row in data:
        print(row)
