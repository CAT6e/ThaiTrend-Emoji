"""
Program: ThaiTrend: Emoji
Version: 1.1 (12 August 2018)
GitHub: https://github.com/CAT6e/ThaiTrend-Emoji
"""

import pickle
import numpy as np
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Segoe UI Emoji"
plt.rcParams.update({'font.size': 16})
plt.rcParams['axes.titlepad'] = 20
plt.rcParams['figure.figsize'] = (12, 8)


def get_percent(values):
    """ Get percent from raw values """
    maximum = max(values)
    percent = []
    for value in values:
        percent.append((value/maximum)*100)
    return percent


def get_data(dictionary, limit, scale=1000000):
    """ Get value from dictionary """
    x_axis = []
    y_axis = []
    
    with open(dictionary, 'rb') as f:
        data = pickle.load(f)
        stmt = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
        count = 0
        for key, value in stmt:
            if limit:
                if count < limit:
                    x_axis.append(key)
                    y_axis.append(value/scale)
                    count += 1
            else:
                x_axis.append(key)
                y_axis.append("{:,}".format(value/scale))
                count += 1
        return x_axis, y_axis


def get_daily(subdir, year, month, emoji):
    """ If you want to visualize data everyday in 1 month, you need to use this 
        [Developer Note]
            This function is in developing. """
    x_pos, x_axis, y_axis = [], [], []
    for i in range(start, end):
        dir = "dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir, year, month, i, subdir)
        with open(dir, 'rb') as f:
            data = pickle.load(f)
            for emo in data:
                if emo == emoji:
                    x_pos.append(i)
                    x_axis.append(emoji)
                    y_axis.append("{:,}".format(data[emo]))
    return x_pos, x_axis, y_axis


def visualizes_usage(year, month, day, total, scale=1000000, decimal=1):
    """
        Visualizes top 10 emojis into bar chart.
        [options]
            If you want to visualize total top emojis => ("2016-2017", False, False)
            If you want to visualize top emojis in one year => (2016 or 2017, False, False)
            If you want to visualize top emojis in one month => (2016 or 2017, 1 -> 12, False)
            If you want to visualize top emojis in one day => (2016 or 2017, 1 -> 12, 1 -> 31)
    """
    month_list = { 1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
    }

    scale_label = {
        1: "Times",
        100: "Hundred Times",
        1000: "Thousand Times",
        1000000: "Million Times",
        1000000000: "Billion Times",
    }

    decimal_label = {
        0: "%d",
        1: "%.1f",
        2: "%.2f",
        3: "%.3f",
    }

    if year == "2016-2018":
        dir = "dictionary/total-usage.pkl"
        title = "Thai top 10 emoji usage on Twitter"
    elif year and not month and not day:
        dir = "dictionary/usage/annually/%04d-usage.pkl" % year
        title = "Thai top 10 emoji usage on Twitter (%04d)" % year 
    elif year and month and not day:
        dir = "dictionary/usage/monthly/%04d-%02d-usage.pkl" % (year, month)
        title = "Thai top 10 emoji usage on Twitter (%s %04d)" % (month_list[month], year)
    else:
        dir = "dictionary/usage/daily/%04d-%02d-%02d-usage.pkl" % (year, month, day)
        title = "Thai top 10 emoji usage on Twitter (%d %s %04d)" % (day, month_list[month], year)
    
    x_axis, y_axis = get_data(dir, 10, scale)

    x_pos = np.arange(total)
    fig, ax = plt.subplots()
    graph = ax.bar(x_pos, y_axis, color='xkcd:lightblue', zorder=1)

    ax.yaxis.grid(color='navy', linestyle='-', linewidth=0.5, alpha=0.25, zorder= 0)
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.get_yaxis().set_major_formatter(FormatStrFormatter(decimal_label[decimal]))

    plt.xlabel('Emoji')
    plt.ylabel('Frequency (%s)' % scale_label[scale])
    plt.title(title)
    plt.xticks(x_pos, x_axis)

    return x_axis, year, month, day, total

def visualizes_behavior(top_usage):
    """
        Visualizes typing behavior into 100percent stacked bar chart.
        [options]
            If you want to visualize total typing behavior => ("2016-2017", False, False)
            If you want to visualize typing behavior in one year => (2016 or 2017, False, False)
            If you want to visualize typing behavior in one month => (2016 or 2017, 1 -> 12, False)
            If you want to visualize typing behavior in one day => (2016 or 2017, 1 -> 12, 1 -> 31)
        [developer note]
            This function is being developed and not be able to call in v0.4.0
    """

    x_axis, year, month, day, total = top_usage

    if year == "2016-2018":
        dir = "dictionary/total-behavior.pkl"
    elif year and not month and not day:
        dir = "dictionary/usage/annually/%04d-behavior.pkl" % year
    elif year and month and not day:
        dir = "dictionary/usage/monthly/%04d-%02d-behavior.pkl" % (year, month)
    else:
        dir = "dictionary/usage/daily/%04d-%02d-%02d-behavior.pkl" % (year, month, day)

    behavior_1 = []
    behavior_2 = []
    behavior_3 = []

    with open(dir, 'rb') as f:
        data = pickle.load(f)
        for emo in x_axis:
            behavior_1.append(data.get(emo).get(1))
            behavior_2.append(data.get(emo).get(2))
            behavior_3.append(data.get(emo).get(3))

    totals = [i+j+k for i,j,k in zip(behavior_1, behavior_2, behavior_3)]

    percent_1 = [i / j * 100 for  i,j in zip(behavior_1, totals)]
    percent_2 = [i / j * 100 for  i,j in zip(behavior_2, totals)]
    percent_3 = [i / j * 100 for  i,j in zip(behavior_3, totals)]
    
    fig, ax = plt.subplots()
    x_pos = np.arange(10)
    p1 = ax.bar(x_pos, percent_1, color = 'xkcd:lightblue')
    p2 = ax.bar(x_pos, percent_2, color = 'xkcd:salmon', bottom = percent_1)
    p3 = ax.bar(x_pos, percent_3, color = 'xkcd:beige', bottom=[i+j for i,j in zip(percent_1, percent_2)])

    plt.xlabel('Emoji')
    plt.ylabel('Usage ratio')
    plt.title('Thai typing behavior based on top 10 emoji')
    plt.xticks(x_pos, x_axis)
    lgd = plt.legend((p1[0], p2[0], p3[0]), ('Once', 'Twice', 'Triple or greater'), loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)

    label = []
    label.append(lgd)


def happiness_index(year, month):
    """
        Visualizes happiness index
        [options]
            If you want to visualize happiness index in one year => (2016 or 2017, False)
            If you want to visualize happiness index in one month => (2016 or 2017, 1 -> 12)
    """
    x_pos, happy, sad, emotion = [], [], [], []

    if year == 2016:
        start = 3
        stop = 13
    elif year == 2018:
        start = 1
        stop = 8
    else:
        start = 1
        stop = 13

    if not month:
        for i in range(start, stop):
            dir = "dictionary/emotion/monthly/%02d-%02d-emotion.pkl" % (year, i)
            with open(dir, 'rb') as f:
                data = pickle.load(f)
                x_pos.append(i)
                happy.append(data['มีความสุข'])
                sad.append(data['ไม่มีความสุข'])
    
    else:
        total_days = monthrange(year, month)[1]
        for i in range(1, total_days+1):
            dir = "dictionary/emotion/monthly/%02d-%02d-emotion.pkl" % (year, month)
            with open(dir, 'rb') as f:
                data = pickle.load(f)
                x_pos.append(i)
                happy.append(data['มีความสุข'])
                sad.append(data['ไม่มีความสุข'])

    totals = [i+j for i,j in zip(happy, sad)]

    percent_1 = [i / j * 100 for  i,j in zip(happy, totals)]
    percent_2 = [i / j * 100 for  i,j in zip(sad, totals)]

    labels = ["Happy ", "Sad"]

    fig, ax = plt.subplots()
    ax.yaxis.grid(color='navy', linestyle='-', linewidth=0.5, alpha=0.25, zorder= 0)
    ax.stackplot(x_pos, percent_1, percent_2, labels=labels, colors=('xkcd:lightblue', 'xkcd:salmon'))
    plt.xticks(x_pos)
    plt.legend(loc=2)

    plt.xlabel('Months')
    plt.ylabel('Emotion ratio')
    plt.title('Thai happiness index on Twitter in %d' % year)


def main():
    """ Program start here """

    # Get all time top 10 emoji usage 
    toptotal = visualizes_usage("2016-2018", False, False, 10)  
    # Get all time typing behavior
    visualizes_behavior(toptotal)

    # Get top 10 emoji usage by year
    visualizes_usage(2018, False, False, 10)
    visualizes_usage(2017, False, False, 10)
    visualizes_usage(2016, False, False, 10)

    # Get top 10 emoji usage by month
    visualizes_usage(2017, 1, False, 10, 1000,0)
    visualizes_usage(2017, 2, False, 10, 1000,0)
    visualizes_usage(2017, 4, False, 10, 1000,0)
    visualizes_usage(2017, 10, False, 10, 1000000,0)

    visualizes_usage(2018, 1, False, 10, 1000,0)
    visualizes_usage(2018, 2, False, 10, 1000,0)
    visualizes_usage(2018, 4, False, 10, 1000,0)

    # Get top 10 emoji usage by day
    visualizes_usage(2017, 1, 1, 10, 1, 0)      #Get 1 jan 2017 usage graph
    visualizes_usage(2017, 2, 14, 10, 1, 0)     #Get 14 feb 2017 usage graph
    visualizes_usage(2017, 4, 13, 10, 1, 0)     #Get 13 apr 2017 usage graph

    # Get happiness index by year
    happiness_index(2018, False)
    happiness_index(2017, False)
    happiness_index(2016, False)

    plt.show()

main()
