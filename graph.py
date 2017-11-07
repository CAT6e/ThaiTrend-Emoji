"""
    Program: ThaiTrend: Emoji v0.2.2 (Alpha test)
    Release Date: 20 October 2017
	Latest Update: 6 November 2017
    Description: This program visualizes dictionary into graph
"""

import pickle

def main():
    with open('dictionary/oct2016-emotion.pkl', 'rb') as f:
        data = pickle.load(f)

main()
