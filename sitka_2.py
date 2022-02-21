import csv
from datetime import datetime

sitka_file = open("sitka_weather_07-2018_simple.csv",'r')

sitka = csv.reader(sitka_file, delimiter = ',')

header_row = next(sitka)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(test_date)


for row in sitka:
    highs.append(int(row[5]))
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)

print(highs)
print(dates)

import matplotlib.pyplot as plt

figure = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

figure.autofmt_xdate()

plt.show()

