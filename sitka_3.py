#1) changing the file to include all the data for the year of 2018
#2) change the title to  - Daily low and high temperatures - 2018
#3) extract low temps from the file and add to chart
#4) shade in the area between high and low


import csv
from datetime import datetime

sitka_file = open("sitka_weather_2018_simple.csv",'r')

sitka = csv.reader(sitka_file, delimiter = ',')

header_row = next(sitka)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

lows = []
highs = []
dates = []

#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(test_date)


for row in sitka:
    lows.append(int(row[6]))
    highs.append(int(row[5]))
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)

print(highs)
print(lows)
print(dates)

import matplotlib.pyplot as plt

figure = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

figure.autofmt_xdate()

#plt.show()

#subplots
plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")


plt.subplot(2,1,2)
plt.plot(dates,highs,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska 2018")

plt.show()
