'''
Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX
columns. Use the header row to determine the indexes for these values, so your program can work
for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
for your graph as well.

create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

Matplotlib's pyplot API has a convenience function called subplots() which acts as a
utility wrapper and helps in creating common layouts of subplots, including the
enclosing figure object, in a single call.

'''

import csv
from datetime import datetime
from email.quoprimime import header_check

sitka_file = open("sitka_weather_2018_simple.csv",'r')

sitka = csv.reader(sitka_file, delimiter = ',')

header_row1 = next(sitka)

print(type(header_row1))

for index, column_header in enumerate(header_row1):
    print(index, column_header)

lows1 = []
highs1 = []
dates1 = []
title1 = next(sitka)[1]

#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(test_date)


for row in sitka:
    lows1.append(int(row[6]))
    highs1.append(int(row[5]))
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates1.append(current_date)

print(highs1)
print(lows1)
print(dates1)


death_file = open("death_valley_2018_simple.csv",'r')

death_valley = csv.reader(death_file, delimiter = ',')

header_row2 = next(death_valley)

print(type(header_row2))

for index, column_header in enumerate(header_row2):
    print(index, column_header)



lows2 = []
highs2 = []
dates2 = []
title2 = next(death_valley)[1]

#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(test_date)


for row in death_valley:
    try:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        
        
    except ValueError:
        print(f"Missing data for {current_date}") 

    else:    
        highs2.append(high)
        lows2.append(low)
        dates2.append(current_date)

print(highs2)
print(lows2)
print(dates2)




import matplotlib.pyplot as plt

figure = plt.figure()


plt.suptitle("Temperature Comparison between Sitka Airport, AK US and Death Valley, CA US", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

#plt.subplots(2)

plt.subplot(2,1,1)

plt.title(title1)
plt.plot(dates1, highs1, c="red")
plt.plot(dates1, lows1, c="blue")
plt.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1)

plt.subplot(2,1,2)

plt.title(title2) 
plt.plot(dates2, highs2, c="red")
plt.plot(dates2, lows2, c="blue")
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

figure.autofmt_xdate()

#plt.show()

#subplots
'''
plt.subplots(2,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")


plt.subplots(2,1)
plt.plot(dates,highs,c="blue")
plt.title("Lows")


plt.suptitle("Highs and Lows of Death Valley, California 2018")
'''
plt.show()


