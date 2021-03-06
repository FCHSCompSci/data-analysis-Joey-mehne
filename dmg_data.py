import csv
from matplotlib import pyplot as plt

filename = 'Overwatch_edopic.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dps_char = []
    char_nme = []
    for row in reader:
        try:
            nme = str(row[0])
            char_nme.append(nme)
            dps = int(row[1])
            dps_char.append(dps)
        except ValueError:
            nme = str(row[0])
            char_nme.append(nme)
            dps = 0
            dps_char.append(dps)

    print(dps_char)
    print(char_nme)


    for index, column_header in enumerate(header_row):
        print(index, column_header)

fig = plt.figure(dpi=128, figsize=(10, 6))
print(len(char_nme))
print(len(dps_char))
plt.plot(dps_char, c='red')
plt.title("Overwatch Hero's Damage per Second", fontsize=24)
plt.xlabel('Hero Name', fontsize=16)
plt.ylabel("Damage", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()