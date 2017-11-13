"""
    Program: ThaiTrend: Emoji v0.3.0 (Alpha test)
    Release Date: 20 October 2017
    Latest Update: 11 November 2017
    Description: This program visualizes dictionary into graph
"""

import pickle
import numpy as np
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Segoe UI Emoji"
plt.rcParams.update({'font.size': 22})
plt.rcParams['axes.titlepad'] = 40
plt.figure(figsize=(20, 10))


def get_percent(values):
    """ Get percent from raw values """
    maximum = max(values)
    percent = []
    for value in values:
        percent.append((value/maximum)*100)
    return percent

def get_behavior():
    """ Get typing behavior usage, total usage is needed """
    x_axis, y_axis = get_value("total-usage.pkl", 10)
    behavior = []
    with open("dictionary/total-behavior.pkl", 'rb') as f:
        data = pickle.load(f)
        for emo in x_axis:
            behavior.append(data.get(emo))


def get_value(dictionary, limit):
    """ Get value from dictionary """
    x_axis = []
    y_axis = []
    filename = "dictionary/%s" % dictionary

    with open(filename, 'rb') as f:
        data = pickle.load(f)
        stmt = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
        count = 0
        for key, value in stmt:
            if count < limit:
                x_axis.append(key)
                y_axis.append(value/1000000)
                count += 1
        return x_axis, y_axis

def visualizes_bar(dictionary, total):
    """ Visualizes data into bar chart """
    x_axis, y_axis = get_value(dictionary, total)

    x_pos = np.arange(total)
    fig, ax = plt.subplots()
    graph = plt.bar(x_pos, y_axis, color='xkcd:azure')

    ax.get_yaxis().set_major_locator(mticker.MultipleLocator(1.8))
    ax.yaxis.grid(color='navy', linestyle='-', linewidth=0.5, alpha=0.25)
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.get_yaxis().set_major_formatter(FormatStrFormatter('%.1f'))
    #ax.set_ybound(1, 24)

    plt.xlabel('Emoji')
    plt.ylabel('Frequency (Million Times)')
    plt.title('Thai top 10 emoji usage on Twitter')
    plt.xticks(x_pos, x_axis)

    plt.show()

def visualizes_stacked():
    """ Visualizes data into stacked bar chart """

    x_axis, y_axis = get_value("total-usage.pkl", 10)

    behavior_1 = []
    behavior_2 = []
    behavior_3 = []

    with open("dictionary/total-behavior.pkl", 'rb') as f:
        data = pickle.load(f)
        for emo in x_axis:
            behavior_1.append(data.get(emo).get(1))
            behavior_2.append(data.get(emo).get(2))
            behavior_3.append(data.get(emo).get(3))

    totals = [i+j+k for i,j,k in zip(behavior_1, behavior_2, behavior_3)]

    percent_1 = [i / j * 100 for  i,j in zip(behavior_1, totals)]
    percent_2 = [i / j * 100 for  i,j in zip(behavior_2, totals)]
    percent_3 = [i / j * 100 for  i,j in zip(behavior_3, totals)]

    x_pos = np.arange(10)
    p1 = plt.bar(x_pos, percent_1, color = 'xkcd:lightblue')
    p2 = plt.bar(x_pos, percent_2, color = 'xkcd:salmon', bottom = percent_1)
    p3 = plt.bar(x_pos, percent_3, color = 'xkcd:beige', bottom=[i+j for i,j in zip(percent_1, percent_2)])

    plt.xlabel('Emoji')
    plt.ylabel('Usage ratio')
    plt.title('Thai typing behavior based on top 10 emoji')
    plt.xticks(x_pos, x_axis)
    lgd = plt.legend((p1[0], p2[0], p3[0]), ('Once', 'Twice', 'Triple or greater'), loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)

    label = []
    label.append(lgd)

    plt.show()


def main():
    """ Program start here """
    visualizes_bar("total-usage.pkl", 10)
    visualizes_stacked()

main()
