import csv
from matplotlib import pyplot as plt

filename = 'Overwatch_edopic.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    average_dmg = 0
    average_dps = []
    for row in reader:
        if 'genji' in row[0].lower():
            average_dps.append(int(row[1]))
            average_dmg = sum(average_dps)/len(average_dps)
    print(average_dps)
    print(average_dmg)


# def get_hero_average(name, dmg_output):