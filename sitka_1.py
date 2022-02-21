import csv

sitka_file = open("sitka_weather_07-2018_simple.csv",'r')

sitka = csv.reader(sitka_file, delimiter = ',')

header_row = next(sitka)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

for row in sitka:
    highs.append(int(row[5]))

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

