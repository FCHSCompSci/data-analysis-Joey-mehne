import csv
from matplotlib import pyplot as plt

filename = 'Overwatch_edopic.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dps_char = []
    for row in reader:
        try:
            dps = int(row[1])
            dps_char.append(dps)
        except ValueError:
            dps = 0
            dps_char.append(dps)

    print(dps_char)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dps_char, c='red')

plt.title("Overwatch Hero's Damage per Second", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Damage", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
