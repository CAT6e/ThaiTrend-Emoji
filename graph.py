"""
    Program: ThaiTrend: Emoji v0.2.2 (Alpha test)
    Release Date: 20 October 2017
    Latest Update: 7 November 2017
    Description: This program visualizes dictionary into graph
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt

def main():
    with open('dictionary/oct2016-emotion.pkl', 'rb') as f:
        data = pickle.load(f)


    def plotgraph():
        line = 19
        emote = ['😀','😅','😢','🙁','😍','😌','😡','😮','😴','😱','🤑','🙄','💩','🙏','👍','👎','👌','🖕','😎']
        freq = [5, 6, 3, 9, 7 ,7, 8, 4, 6, 7, 3, 9, 1, 9, 10, 12, 7, 11, 1]
        x_pos = np.arange(line)
        fig, ax = plt.subplots()

        graph = plt.bar(x_pos, freq, color='green')
        ax.yaxis.grid(color='k', linestyle='-', linewidth=0.2)

        plt.xlabel('Emote')
        plt.ylabel('Frequency')
        plt.title('THAI TREND')
        plt.xticks(x_pos, emote)

        plt.show()

    plotgraph()

main()
