import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/New_York.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取数据，最高温度和最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据最高温度和最低温度绘制图形
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['simhei']
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形格式
title = "2021年每日最高温度和最低温度\n中央公园 美国 纽约"
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("温度 (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()