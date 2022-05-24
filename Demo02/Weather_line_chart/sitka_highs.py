import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
    print(highs)
# 根据最高温度绘制图表
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['simhei']
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# 设置图形的格式
plt.title("2018年每日最高温度",fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("温度 (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
