"""
Collector module handles the execution's code that analyzes tweets.
"""

# 3rd-Party modules
import emoji

# Pickle is used for saving result
import pickle

def analyze(filenames, usage = {}, behavior = {}, happiness = {}):
	""" Analyze tweet by input the list of filenames, use time_picker() to select time. """

	daily_tweet = "../{}.log".format(filenames)
	
	with open(daily_tweet, "r", encoding="utf8", errors='ignore') as tweet:
		line = tweet.readline()

		while line:

			# Get emoji that found in the tweet
			emoji_found = [emo for emo in line if emo in emoji.UNICODE_EMOJI]

			# Collect emoji usage data
			emoji_usage(emoji_found, usage)
			# Collect emotion from found emoji
			emotion(emoji_found, happiness)
			# Collect emoji typing behavior
			typing_behavior(emoji_found, behavior)

			line = tweet.readline()

	export_filename = filenames.split("/")
	export_filename = export_filename[1]
	export_dict(usage, "ThaiTrend-Emoji/dictionary/usage/daily/%s-usage.pkl" % export_filename)
	export_dict(behavior, "ThaiTrend-Emoji/dictionary/behavior/daily/%s-behavior.pkl" % export_filename)
	export_dict(happiness, "ThaiTrend-Emoji/dictionary/emotion/daily/%s-emotion.pkl" % export_filename)


def emoji_usage(emoji_list, output_dict):
	""" Collect emoji usage """
	for emo in emoji_list:
		if emo not in output_dict:
			output_dict[emo] = 1
		else:
			output_dict[emo] += 1
		return output_dict


def typing_behavior(emoji_list, output_dict):
	""" Collect typing behavior """
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


def emotion(input_list, output_dict):
	""" Collect emotion from emoji """
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


def export_dict(dictionary, url):
	""" Export processed data to pickle file """
	pickle.dump(dictionary, open(url, "wb"))
