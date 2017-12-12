"""
	Program: ThaiTrend: Emoji
	Description: ThaiTrend: Emoji is a data analysis project which analyze Thai tweets
	Latest Update: 12 December 2017 (v1.0)
"""

import pickle
import emoji

def time_picker(monthstart, yearstart, monthend, yearend):
	""" Get the certain period of time """
	files = list()

	if yearstart < yearend:
		for month in range(monthstart, 13):
			for day in range(1, 32):
				files.append("2016-%02d-%02d" % (month, day))
		for month in range(1, monthend+1):
			for day in range(1, 32):
				files.append("2017-%02d-%02d" % (month, day))
	else:
		for month in range(monthstart, monthend+1):
			for day in range(1, 32):
				files.append("%04d-%02d-%02d" % (yearstart, month, day))

	return files


def export_dict(dictionary, url):
	""" Export processed data to pickle file """
	pickle.dump(dictionary, open(url, "wb"))


def emotion(input_list, output_dict):
	"""
		Get emotion from emoji
	"""
	emotion_mapping = {"😀":"มีความสุข",
	"😃":"มีความสุข",
	"😄":"มีความสุข",
	"😁":"มีความสุข",
	"😆":"มีความสุข",
	"😅":"มีความสุข",
	"😂":"มีความสุข",
	"🤣":"มีความสุข",
	"😊":"มีความสุข",
	"😇":"มีความสุข",
	"🙂":"มีความสุข",
	"🙃":"มีความสุข",
	"😉":"มีความสุข",
	"😌":"มีความสุข",
	"😍":"มีความสุข",
	"😘":"มีความสุข",
	"😗":"มีความสุข",
	"😙":"มีความสุข",
	"😚":"มีความสุข",
	"😋":"มีความสุข",
	"😜":"มีความสุข",
	"😝":"มีความสุข",
	"😛":"มีความสุข",
	"🤗":"มีความสุข",
	"🤓":"มีความสุข",
	"😎":"มีความสุข",
	"🤡":"มีความสุข",
	"🤠":"มีความสุข",
	"😒":"ไม่มีความสุข",
	"😞":"ไม่มีความสุข",
	"😔":"ไม่มีความสุข",
	"😟":"ไม่มีความสุข",
	"☹" :"ไม่มีความสุข",
	"😕":"ไม่มีความสุข",
	"🙁":"ไม่มีความสุข",
	"😣":"ไม่มีความสุข",
	"😖":"ไม่มีความสุข",
	"😫":"ไม่มีความสุข",
	"😩":"ไม่มีความสุข",
	"😤":"ไม่มีความสุข",
	"😠":"ไม่มีความสุข",
	"😡":"ไม่มีความสุข",
	"😐":"ไม่มีความสุข",
	"😑":"ไม่มีความสุข",
	"😯":"ไม่มีความสุข",
	"😦":"ไม่มีความสุข",
	"😧":"ไม่มีความสุข",
	"😮":"มีความสุข",
	"😲":"มีความสุข",
	"😵":"ไม่มีความสุข",
	"😳":"มีความสุข",
	"😱":"ไม่มีความสุข",
	"😨":"ไม่มีความสุข",
	"😰":"ไม่มีความสุข",
	"😢":"ไม่มีความสุข",
	"😥":"ไม่มีความสุข",
	"🤤":"ไม่มีความสุข",
	"😭":"ไม่มีความสุข",
	"😓":"ไม่มีความสุข",
	"😪":"ไม่มีความสุข",
	"😴":"ไม่มีความสุข",
	"🤥":"ไม่มีความสุข",
	"😬":"มีความสุข",
	"🤢":"ไม่มีความสุข",
	"🤧":"ไม่มีความสุข",
	"😷":"ไม่มีความสุข",
	"🤒":"ไม่มีความสุข",
	"🤕":"ไม่มีความสุข",
	"😈":"ไม่มีความสุข",
	"👿":"ไม่มีความสุข",
	"👹":"ไม่มีความสุข",
	"👺":"ไม่มีความสุข",
	"💩":"ไม่มีความสุข",
	"😺":"มีความสุข",
	"😸":"มีความสุข",
	"😹":"มีความสุข",
	"😻":"มีความสุข",
	"😼":"มีความสุข",
	"😽":"มีความสุข",
	"🙀":"มีความสุข",
	"😿":"ไม่มีความสุข",
	"😾":"ไม่มีความสุข",
	"👏":"มีความสุข",
	"👍":"มีความสุข",
	"👎":"ไม่มีความสุข",
	"🖕":"ไม่มีความสุข",
	"❤":"มีความสุข",
	"💛":"มีความสุข",
	"💚":"มีความสุข",
	"💙":"มีความสุข",
	"💜":"มีความสุข",
	"🖤":"ไม่มีความสุข",
	"💕":"มีความสุข",
	"💞":"มีความสุข",
	"💓":"มีความสุข",
	"💗":"มีความสุข",
	"💖":"มีความสุข",
	"💘":"มีความสุข",
	"💝":"มีความสุข",
	"💟":"มีความสุข"}

	for emo in input_list:
		if emo in emotion_mapping:
			feeling = emotion_mapping[emo]
			if feeling not in output_dict:
				output_dict[feeling] = 1
			else:
				output_dict[feeling] += 1

	return output_dict


def emoji_usage(emoji_list, output_dict):
	""" Record emoji usage """
	for emo in emoji_list:
		if emo not in output_dict:
			output_dict[emo] = 1
		else:
			output_dict[emo] += 1
		return output_dict


def typing_behavior(emoji_list, output_dict):
	""" Record typing behavior """
	emoji_list.append(" ")
	repeated = 1
	for position in range(len(emoji_list)-1):
		start = emoji_list[position]
		nexts = emoji_list[position+1]
		if start == nexts:
			repeated += 1
		else:
			if repeated > 3:
				repeated = 3
			if start not in output_dict:
				output_dict[start] = {}
				output_dict[start][1] = 0
				output_dict[start][2] = 0
				output_dict[start][3] = 0
			output_dict[start][repeated] += 1
			repeated = 1
	return output_dict


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
		for day in range(1, 32):
			files1.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[0], year, month, day, subdir[0]))
			files2.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[1], year, month, day, subdir[1]))
			files3.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[2], year, month, day, subdir[2]))
				
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

		export_dict(dict1, "dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[0], year, month, subdir[0]))
		export_dict(dict2, "dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[1], year, month, subdir[1]))
		export_dict(dict3, "dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[2], year, month, subdir[2]))
	
	else:
		files1 = []
		dict1 = {}
		for day in range(1, 32):
			files1.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir, year, month, day, subdir))

		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += 1

		export_dict(dict1, "dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir, year, month, subdir))


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
	else:
		start = 1
		stop = 11

	if isinstance(subdir, list):
		files1, files2, files3 = [], [], []
		dict1, dict2, dict3 = {}, {}, {}

		for month in range(start, stop):
			files1.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[0], year, month, subdir[0]))
			files2.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[1], year, month, subdir[1]))
			files3.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[2], year, month, subdir[2]))
		
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
		export_dict(dict1, "dictionary/%s/annually/%04d-%s.pkl" % (subdir[0], year, subdir[0]))
		export_dict(dict2, "dictionary/%s/annually/%04d-%s.pkl" % (subdir[1], year, subdir[1]))
		export_dict(dict3, "dictionary/%s/annually/%04d-%s.pkl" % (subdir[2], year, subdir[2]))
	
	else:
		files1 = []
		dict1 = {}
		for month in range(start, stop):
			files1.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir, year, month, subdir))

		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += data[element]

		export_dict(dict1, "dictionary/%s/annually/%04d-%s.pkl" % (subdir, year, subdir))


def zip_total(subdir):
	"""
		Merge annually dictionaries to get total dictionaries, annually dictionaries is required
		[option]
			subdir: Identify dict type; usage, behavior or emotion
	"""

	if isinstance(subdir, list):
		files1, files2, files3 = [], [], []
		dict1, dict2, dict3 = {}, {}, {}
		for year in range(2016, 2018):
			files1.append("dictionary/%s/annually/%04d-%s.pkl" % (subdir[0], year, subdir[0]))
			files2.append("dictionary/%s/annually/%04d-%s.pkl" % (subdir[1], year, subdir[1]))
			files3.append("dictionary/%s/annually/%04d-%s.pkl" % (subdir[2], year, subdir[2]))

		for filename in files1:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict1:
						dict1[element] = data[element]
					else:
						dict1[element] += data[element]
		export_dict(dict1, "dictionary/total-%s.pkl" % (subdir[0]))

		for filename in files2:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict2:
						dict2[element] = data[element]
					else:
						for sub_element in dict2[element]:
							dict2[element][sub_element] += data[element][sub_element]
		export_dict(dict2, "dictionary/total-%s.pkl" % (subdir[1]))

		for filename in files3:
			with open(filename, 'rb') as f:
				data = pickle.load(f)
				for element in data:
					if element not in dict3:
						dict3[element] = data[element]
					else:
						dict3[element] += data[element]
		export_dict(dict3, "dictionary/total-%s.pkl" % (subdir[2]))
	
	else:
		files1 = []
		dict1 = {}
		for year in range(2016, 2018):
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


def analyze(filename):
	"""
		Analyze tweet by input the list of filename, use time_picker() to select time.
	"""

	usage = {}
	behavior = {}
	happiness = {}

	day_count = 0
	for data in filename:
		day_count += 1
		daily_tweet = "data/"+data+".log"
		with open(daily_tweet, "r", encoding="utf8", errors='ignore') as tweet:
			line = tweet.readline()

			while line:

				emoji_found = [emo for emo in line if emo in emoji.UNICODE_EMOJI]

				#get_usage
				emoji_usage(emoji_found, usage)
				#get_emotion
				emotion(emoji_found, happiness)
				#get_behavior
				typing_behavior(emoji_found, behavior)

				line = tweet.readline()

		export_dict(usage, "dictionary/usage/daily/%s-usage.pkl" % data)
		export_dict(behavior, "dictionary/behavior/daily/%s-behavior.pkl" % data)
		export_dict(happiness, "dictionary/emotion/daily/%s-emotion.pkl" % data)


def main():
	""" The program starts here. """

	#analyze(time_picker(3, 2016, 10, 2017))


	for month in range(3, 13):
		zip_monthly(["usage", "behavior", "emotion"], month, 2016)
	for month in range(1, 11):
		zip_monthly(["usage", "behavior", "emotion"], month, 2017)

	zip_annually(["usage", "behavior", "emotion"], 2016)
	zip_annually(["usage", "behavior", "emotion"], 2017)

	zip_total(["usage", "behavior", "emotion"])

main()
