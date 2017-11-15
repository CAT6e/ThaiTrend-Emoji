"""
	Program: ThaiTrend: Emoji
	Latest Update: 15 November 2017
	Description: ThaiTrend: Emoji is a data analysis project which analyze Thai tweets
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


def emotion(emoji_list, output_dict):
	""" Get emotion from emoji
		map emotion ใหม่ให้เหลือแค่ "มีความสุข" กับ "ไม่มีความสุข"
		อีโมจิที่ไม่เข้าทั้งสองกลุ่มนี้ลบออกได้เลย
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
	"🤑":"ไม่มีความสุข",
	"🤗":"มีความสุข",
	"🤓":"มีความสุข",
	"😎":"มีความสุข",
	"🤡":"มีความสุข",
	"🤠":"มีความสุข",
	"😏":"ไม่มีความสุข",
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
	"😶":"ไม่มีความสุข",
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
	"🙄":"ไม่มีความสุข",
	"🤔":"ไม่มีความสุข",
	"🤥":"ไม่มีความสุข",
	"😬":"ไม่มีความสุข",
	"🤐":"ไม่มีความสุข",
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
	"🙀":"ไม่มีความสุข",
	"😿":"ไม่มีความสุข",
	"😾":"ไม่มีความสุข",
	"👐":"มีความสุข",
	"🙌":"มีความสุข",
	"👏":"มีความสุข",
	"🙏":"มีความสุข",
	"👍":"มีความสุข",
	"👎":"ไม่มีความสุข",
	"👌":"มีความสุข",
	"🖕":"ไม่มีความสุข",
	"❤":"ไม่มีความสุข",
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

	for emo in emoji_list:
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
	repeated = 1
	for position in range(len(emoji_list)):
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

	files = []
	monthly_dict = {}

	if isinstance(subdir, list):
		for month in range(1, 13):
			files.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[0], year, month, day, subdir))
			files.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[1], year, month, day, subdir))
			files.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir[2], year, month, day, subdir))
	else:
		for day in range(1, 32):
			files.append("dictionary/%s/daily/%04d-%02d-%02d-%s.pkl" % (subdir, year, month, day, subdir))

	for filename in files:
	    with open(filename, 'rb') as f:
	        data = pickle.load(f)
	        monthly_dict.update(data)

	export_dict(monthly_dict, "dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir, year, month, subdir))


def zip_annually(subdir, year):
	"""
		Merge monthly dictionaries into annually dictionary, monthly dictionaries is required
		[option]
			subdir: Identify dict type; usage, behavior or emotion
			year: Your target year
	"""

	files = []
	annually_dict = {}

	if isinstance(subdir, list):
		for month in range(1, 13):
			files.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[0], year, month, subdir))
			files.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[1], year, month, subdir))
			files.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir[2], year, month, subdir))
	else:
		for month in range(1, 13):
			files.append("dictionary/%s/monthly/%04d-%02d-%s.pkl" % (subdir, year, month, subdir))

	for filename in files:
	    with open(filename, 'rb') as f:
	        data = pickle.load(f)
	        annually_dict.update(data)

	export_dict(annually_dict, "dictionary/%s/annually/%04d-%02d-%s.pkl" % (subdir, year, month, subdir))


def analyze(filename):
	"""
		Analyze tweet by input the list of filename, use time_picker() to select time.
	"""

	usage = {}
	behavior = {}

	day_count = 0
	for data in filename:
		day_count += 1
		daily_tweet = "data/"+data+".log"
		with open(daily_tweet, "r", encoding="utf8", errors='ignore') as tweet:
			line = tweet.readline()
			emoji_per_day = dict()

			while line:

				emoji_found = [emo for emo in line if emo in emoji.UNICODE_EMOJI]

				#get_usage
				emoji_usage(emoji_found, usage)
				get_emotion
				emotion(emoji_found, emoji_per_day)
				get_behavior
				typing_behavior(emoji_found, behavior)

				line = tweet.readline()

		#get_emotion
		total_emoji_in_one_day = sum(emoji_per_day.values())
		maximum_emoji = max(emoji_per_day, key=emoji_per_day.get)
		maximum_value = emoji_per_day[maximum_emoji]
		percentage = (maximum_value/total_emoji_in_one_day)*100

		emo[day_count] = {maximum_emoji:maximum_value}

		export_dict(usage, "dictionary/usage/daily/%s-usage.pkl" % data)
		export_dict(behavior, "dictionary/behavior/daily/%s-behavior.pkl" % export_name)
		export_dict(emo, "dictionary/emotion/daily/%s-emotion.pkl" % export_name)


def main():
	""" The program starts here. """
	analyze(time_picker(3, 2016, 10, 2017))

	for month in range(3, 13):
		zip_monthly("[usage, behavior, emotion]", month, 2016)
	for month in range(1, 11):
		zip_monthly("[usage, behavior, emotion]", month, 2017)

	zip_annually("[usage, behavior, emotion]", 2016)
	zip_annually("[usage, behavior, emotion]", 2017)

main()
