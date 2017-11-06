"""
	Program: ThaiTrend: Emoji v0.2.2 (Alpha test)
	Release Date: 20 October 2017
	Latest Update: 5 November 2017
	Description: ThaiTrend: Emoji is a data analysis project which analyze Thai tweets
"""

import pickle


def emotion():
	""" Get emotion from emoji """
	emotion_mapping = {"😀":"มีความสุข",
	"😃":"มีความสุข",
	"😄":"มีความสุข",
	"😁":"มีความสุข",
	"😆":"สนุก",
	"😅":"สนุก",
	"😂":"สนุก",
	"🤣":"สนุก",
	"😊":"มีความสุข",
	"😇":"มีความสุข",
	"🙂":"มีความสุข",
	"🙃":"มีความสุข",
	"😉":"มีความสุข",
	"😌":"ผ่อนคลาย",
	"😍":"รู้สึกรัก",
	"😘":"รู้สึกรัก",
	"😗":"ผ่อนคลาย",
	"😙":"ผ่อนคลาย",
	"😚":"ผ่อนคลาย",
	"😋":"มีความสุข",
	"😜":"สนุก",
	"😝":"สนุก",
	"😛":"สนุก",
	"🤑":"รู้สึกหิว",
	"🤗":"มีความสุข",
	"🤓":"ผ่อนคลาย",
	"😎":"ผ่อนคลาย",
	"🤡":"มีความสุข",
	"🤠":"มีความสุข",
	"😏":"smirk",
	"😒":"smirk",
	"😞":"รู้สึกผิดหวัง",
	"😔":"รู้สึกผิดหวัง",
	"😟":"รู้สึกเสียใจ",
	"☹" : "รู้สึกเสียใจ",
	"😕":"รู้สึกเสียใจ",
	"🙁":"รู้สึกเสียใจ",
	"😣":"รู้สึกโกรธ",
	"😖":"รู้สึกเสียใจ",
	"😫":"รู้สึกผิดหวัง",
	"😩":"รู้สึกผิดหวัง",
	"😤":"รู้สึกผิดหวัง",
	"😠":"รู้สึกโกรธ",
	"😡":"รู้สึกโกรธ",
	"😶":"pokerface",
	"😐":"pokerface",
	"😑":"pokerface",
	"😯":"รู้สึกประหลาดใจ",
	"😦":"รู้สึกเสียใจ",
	"😧":"รู้สึกเสียใจ",
	"😮":"รู้สึกประหลาดใจ",
	"😲":"รู้สึกประหลาดใจ",
	"😵":"รู้สึกประหลาดใจ",
	"😳":"รู้สึกรัก",
	"😱":"รู้สึกประหลาดใจ",
	"😨":"รู้สึกประหลาดใจ",
	"😰":"ป่วย",
	"😢":"รู้สึกเสียใจ",
	"😥":"รู้สึกเสียใจ",
	"🤤":"รู้สึกหิว",
	"😭":"รู้สึกเสียใจ",
	"😓":"รู้สึกเสียใจ",
	"😪":"รู้สึกง่วงนอน",
	"😴":"รู้สึกง่วงนอน",
	"🙄":"มองบน",
	"🤔":"พยายามใช้ความคิด",
	"🤥":"โกหก",
	"😬":"สนุก",
	"🤐":"เงียบ",
	"🤢":"ป่วย",
	"🤧":"ป่วย",
	"😷":"ป่วย",
	"🤒":"ป่วย",
	"🤕":"ป่วย",
	"😈":"รู้สึกโกรธ",
	"👿":"รู้สึกโกรธ",
	"👹":"รู้สึกโกรธ",
	"👺":"รู้สึกโกรธ",
	"💩":"aunji",
	"😺":"มีความสุข",
	"😸":"มีความสุข",
	"😹":"สนุก",
	"😻":"รู้สึกรัก",
	"😼":"มีความสุข",
	"😽":"ผ่อนคลาย",
	"🙀":"รู้สึกประหลาดใจ",
	"😿":"รู้สึกเสียใจ",
	"😾":"รู้สึกโกรธ",
	"👐":"ผ่อนคลาย",
	"🙌":"ผ่อนคลาย",
	"👏":"รู้สึกชอบ",
	"🙏":"ไหว้",
	"👍":"รู้สึกชอบ",
	"👎":"รู้สึกชอบ",
	"👌":"OK",
	"🖕":"middlefinger",
	"❤":"รู้สึกรัก",
	"💛":"รู้สึกรัก",
	"💚":"รู้สึกรัก",
	"💙":"รู้สึกรัก",
	"💜":"รู้สึกรัก",
	"🖤":"รู้สึกรัก",
	"💕":"รู้สึกรัก",
	"💞":"รู้สึกรัก",
	"💓":"รู้สึกรัก",
	"💗":"รู้สึกรัก",
	"💖":"รู้สึกรัก",
	"💘":"รู้สึกรัก",
	"💝":"รู้สึกรัก",
	"💟":"รู้สึกรัก"}
	return emotion_mapping


def loopfiles(monthstart, monthend, year):
	""" Loop filename """
	files = list()
	for month in range(monthstart, monthend+1):
		for day in range(1, 32):
			files.append("data/%04d-%02d-%02d.log" % (year, month, day))
	return files


def export_dict(dictionary, url):
	""" Export processed data to pickle file """
	pickle.dump(dictionary, open(url, "wb"))


def emoji_usage(char, emoji):
	""" Record emoji usage """
	if char not in emoji:
		emoji[char] = 1
	else:
		emoji[char] += 1
	return emoji


def main():
	""" The program starts here. """

	#Get filename of certain time

	thai_tweets_from_2016 = loopfiles(3, 12, 2016) #loop filename from 2016-03-01.log to 2017-10-31.log
	for i in loopfiles(1, 10, 2017):
		thai_tweets_from_2016.append(i)

	jan2017 = loopfiles(1, 1, 2017)
	feb2017 = loopfiles(2, 2, 2017)
	apr2017 = loopfiles(4, 4, 2017)

	oct2016 = loopfiles(10, 10, 2016)
	oct2017 = loopfiles(10, 10, 2017)

	#Analyze the most used emoji and typing behavior from 2016-03-01 to 2017-10-31
	analyze(thai_tweets_from_2016, "usage behavior", "total")

	analyze(jan2017, "usage", "jan2017") #Analyze the most used emoji in January 2017 (New Year's festival analyze)
	analyze(feb2017, "usage", "feb2017") #Analyze the most used emoji in February 2017 (Valentine's festival analyze)
	analyze(apr2017, "usage", "apr2017") #Analyze the most used emoji in April 2017 (songkarn's festival analyze)

	analyze(oct2016, "emotion", "oct2016") #Analyze thai emotion in October 2016
	analyze(oct2017, "emotion", "oct2017") #Analyze thai emotion in October 2017


def analyze(filename, options, export_name):
	"""
	Analyze tweet by input the list of filename and options, seperated by space:
		Filename:
			Use loopfiles() to get list filename

		Options:
			usage - to get the most used emoji**
			behavior - to get typing behavior
			emotion - to get the most used emoji categorized by emotion

		Export name:
			Program will export dictionary in "export_name-options.pkl" format.
			Example:
				if export_name = 2017 and options = usage
				Your file is "2017-usage.pkl"
	"""
	get_usage = False
	get_behavior = False
	get_emotion = False

	option = options.split(" ")
	if "usage" in option:
		get_usage = True
		emoji = dict()

	if "behavior" in option:
		get_behavior = True
		behavior = dict()

	if "emotion" in option:
		get_emotion = True
		emo = dict()
		emotion_mapping = emotion()

	day_count = 0
	for data in filename:
		day_count += 1
		with open(data, "r", encoding="utf8", errors='ignore') as tweet:
			line = tweet.readline()
			if get_emotion:
				emoji_per_day = dict()

			while line:
				if get_behavior:
					previous_emoji = False
					repeated = 1

				for char in line:
					if ord(char) >= 127744 and ord(char) <= 129355:
						if get_usage:
							emoji_usage(char, emoji)

						if get_emotion and char in emotion_mapping:
							feeling = emotion_mapping[char]
							if feeling not in emoji_per_day:
								emoji_per_day[feeling] = 1
							else:
								emoji_per_day[feeling] += 1

						if get_behavior:
							if previous_emoji != char:
								if previous_emoji:
									if repeated > 3:
										repeated = 3
									if previous_emoji not in behavior:
										behavior[previous_emoji] = {}
										behavior[previous_emoji][1] = 0
										behavior[previous_emoji][2] = 0
										behavior[previous_emoji][3] = 0
									behavior[previous_emoji][repeated] += 1
								previous_emoji = char
								repeated = 1
							else:
								repeated += 1

				if get_behavior:
					if previous_emoji:
						if repeated > 3:
							repeated = 3
						if previous_emoji not in behavior:
							behavior[previous_emoji] = {}
							behavior[previous_emoji][1] = 0
							behavior[previous_emoji][2] = 0
							behavior[previous_emoji][3] = 0
						behavior[previous_emoji][repeated] += 1

				line = tweet.readline()

		if get_emotion:
			total_emoji_in_one_day = sum(emoji_per_day.values())
			maximum_emoji = max(emoji_per_day, key=emoji_per_day.get)
			maximum_value = emoji_per_day[maximum_emoji]

			percentage = (maximum_value/total_emoji_in_one_day)*100

			emo[day_count] = {maximum_emoji:maximum_value}

	#months = { 1: "JAN",
	#2: "FEB",
	#3: "MAR",
	#4: "APR",
	#5: "MAY",
	#6: "JUN",
	#7: "JUL",
	#8: "AUG",
	#9: "SEP",
	#10: "OCT",
	#11: "NOV",
	#12: "DEC",
	#}


	if get_usage:
		export_dict(emoji, "dictionary/%s-usage.pkl" % export_name)
	if get_behavior:
		export_dict(behavior, "dictionary/%s-behavior.pkl" % export_name)
	if get_emotion:
		export_dict(emo, "dictionary/%s-emotion.pkl" % export_name)


main()
