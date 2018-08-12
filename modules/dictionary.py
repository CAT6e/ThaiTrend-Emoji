"""
Dictionary module handles dictionary that is saved into pickle (.pkl) file.
"""

import pickle
from calendar import monthrange

def zipper(start_month, start_year, end_month, end_year):
	""" The main function when zipping individual pickle files """
	same_year = False
	year_difference = end_year-start_year

	# End year must not be less than the start year
	if year_difference < 0:
		print("Error: Zipper cannot work, invalid time.")
		return

	if year_difference == 0:
		same_year = True

	if same_year:
		for month in range(start_month, end_month+1):
			zip_monthly(["usage", "behavior", "emotion"], month, start_year)
		zip_annually(["usage", "behavior", "emotion"], start_year)

	else:
		for year_count in range(year_difference+1):
			if start_year != end_year and year_count == 0:
				for month in range(start_month, 13):
					zip_monthly(["usage", "behavior", "emotion"], month, start_year)
			elif start_year != end_year and year_count == 1:
				for month in range(1, 13):
					zip_monthly(["usage", "behavior", "emotion"], month, start_year)
			else:
				for month in range(1, end_month+1):
					zip_monthly(["usage", "behavior", "emotion"], month, start_year)
			zip_annually(["usage", "behavior", "emotion"], start_year)
			start_year += 1

	zip_total(["usage", "behavior", "emotion"])


def zip_monthly(subdir, month, year):
	"""
		Merge daily dictionaries into monthly dictionaries.
		[option]
			subdir: Identify dict type; usage, behavior or emotion
			month: Your target month
			year: Your target year
	"""

	if isinstance(subdir, list):
		files1, files2, files3 = [], [], []
		dict1, dict2, dict3 = {}, {}, {}
		total_days = monthrange(year, month)[1]
		for day in range(1, total_days+1):
			files1.append("ThaiTrend-Emoji/dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[0], year, month, day, subdir[0]))
			files2.append("ThaiTrend-Emoji/dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[1], year, month, day, subdir[1]))
			files3.append("ThaiTrend-Emoji/dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[2], year, month, day, subdir[2]))
		
		print(files1)
				
		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += data[element]

		for filename in files2:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict2:
						dict2[element] = data[element]
					else:
						for sub_element in dict2[element]:
							dict2[element][sub_element] += data[element][sub_element]

		for filename in files3:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict3:
						dict3[element] = data[element]
					else:
						dict3[element] += data[element]

		export_dict(dict1, "ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[0], year, month, subdir[0]))
		export_dict(dict2, "ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[1], year, month, subdir[1]))
		export_dict(dict3, "ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[2], year, month, subdir[2]))
	
	else:
		files1 = []
		dict1 = {}
		total_days = monthrange(year, month)[1]
		for day in range(1, total_days+1):
			files1.append("ThaiTrend-Emoji/dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir, year, month, day, subdir))

		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += 1

		export_dict(dict1, "ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir, year, month, subdir))


def zip_annually(subdir, year):
	"""
		Merge monthly dictionaries into annually dictionary, monthly dictionaries is required
		[option]
			subdir: Identify dict type; usage, behavior or emotion
			year: Your target year
	"""

	if year == 2016:
		start = 3
		stop = 13
	elif year == 2018:
		start = 1
		stop = 8
	else:
		start = 1
		stop = 13

	if isinstance(subdir, list):
		files1, files2, files3 = [], [], []
		dict1, dict2, dict3 = {}, {}, {}

		for month in range(start, stop):
			files1.append("ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[0], year, month, subdir[0]))
			files2.append("ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[1], year, month, subdir[1]))
			files3.append("ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[2], year, month, subdir[2]))
		
		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += data[element]
		for filename in files2:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict2:
						dict2[element] = data[element]
					else:
						for sub_element in dict2[element]:
							dict2[element][sub_element] += data[element][sub_element]
		for filename in files3:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict3:
						dict3[element] = data[element]
					else:
						dict3[element] += data[element]
		export_dict(dict1, "ThaiTrend-Emoji/dictionary/%s/annually/%04d-%s.pkl" % (subdir[0], year, subdir[0]))
		export_dict(dict2, "ThaiTrend-Emoji/dictionary/%s/annually/%04d-%s.pkl" % (subdir[1], year, subdir[1]))
		export_dict(dict3, "ThaiTrend-Emoji/dictionary/%s/annually/%04d-%s.pkl" % (subdir[2], year, subdir[2]))
	
	else:
		files1 = []
		dict1 = {}
		for month in range(start, stop):
			files1.append("ThaiTrend-Emoji/dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir, year, month, subdir))

		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += data[element]

		export_dict(dict1, "ThaiTrend-Emoji/dictionary/%s/annually/%04d-%s.pkl" % (subdir, year, subdir))


def zip_total(subdir):
	"""
		Merge annually dictionaries to get total dictionaries, annually dictionaries is required
		[option]
			subdir: Identify dict type; usage, behavior or emotion
	"""

	if isinstance(subdir, list):
		files1, files2, files3 = [], [], []
		dict1, dict2, dict3 = {}, {}, {}
		for year in range(2016, 2019):
			files1.append("ThaiTrend-Emoji/dictionary/%s/annually/%04d-%s.pkl" % (subdir[0], year, subdir[0]))
			files2.append("ThaiTrend-Emoji/dictionary/%s/annually/%04d-%s.pkl" % (subdir[1], year, subdir[1]))
			files3.append("ThaiTrend-Emoji/dictionary/%s/annually/%04d-%s.pkl" % (subdir[2], year, subdir[2]))

		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += data[element]
		export_dict(dict1, "ThaiTrend-Emoji/dictionary/total-%s.pkl" % (subdir[0]))

		for filename in files2:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict2:
						dict2[element] = data[element]
					else:
						for sub_element in dict2[element]:
							dict2[element][sub_element] += data[element][sub_element]
		export_dict(dict2, "ThaiTrend-Emoji/dictionary/total-%s.pkl" % (subdir[1]))

		for filename in files3:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict3:
						dict3[element] = data[element]
					else:
						dict3[element] += data[element]
		export_dict(dict3, "ThaiTrend-Emoji/dictionary/total-%s.pkl" % (subdir[2]))
	
	else:
		files1 = []
		dict1 = {}
		for year in range(2016, 2019):
			files1.append("dictionary/%s/annually/%04d-%s.pkl" % (subdir, year, subdir))

		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += data[element]
		export_dict(dict1, "dictionary/total-%s.pkl" % (subdir))


def export_dict(dictionary, url):
	""" Export processed data to pickle file """
	pickle.dump(dictionary, open(url, "wb"))

