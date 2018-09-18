import csv

with open('mpg.csv') as file:
    csv.reader(file)
    mpg_reader = csv.reader(file)
    for row in mpg_reader:
        print(row)
