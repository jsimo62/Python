import csv

vehicles = {'compact': 0, 'compact_num': 0}
with open('mpg.csv') as file:
    mpg_reader = csv.reader(file)
    next(mpg_reader) # skipping the first line
    for row in mpg_reader:
        if row[11] == 'compact':
            vehicles['compact'] = vehicles['compact'] + int(row[8])
            vehicles['compact_num'] = vehicles['compact_num'] + 1


print(vehicles)
print('avg city milage for compact ', vehicles['compact']/vehicles['compact_num'])
