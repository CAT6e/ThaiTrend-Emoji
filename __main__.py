"""
Program: ThaiTrend: Emoji
Version: 1.1 (12 August 2018)
GitHub: https://github.com/CAT6e/ThaiTrend-Emoji
"""

# ThaiTrend: Emoji's modules
from .modules import dictionary, collector

# For Time Picker
from calendar import monthrange
import datetime

# Python's multiprocessing (Parallel processing) and helping modules
import multiprocessing as mp
import platform
import time
import os

def time_picker(start_month, start_year, end_month, end_year):
	"""
	This function loops filenames from given parameters.
	These filenames are represented the twiiter log files' name.
	"""

	filenames = list()
	same_year = False

	year_difference = end_year-start_year

	# End year must not be less than the start year
	if year_difference < 0:
		return "Error: Time_Picker cannot work, invalid time picking."
	
	if year_difference == 0:
		same_year = True

	if same_year:
		for month in range(start_month, end_month+1):
				total_days = monthrange(start_year, month)[1]
				for day in range(1, total_days+1):
					filenames.append("%04d-%02d/%04d-%02d-%02d" % (start_year, month, start_year, month, day))
	else:
		for year_loop in range(year_difference+1):
			if start_year != end_year and year_loop == 0:
				for month in range(start_month, 13):
					total_days = monthrange(start_year, month)[1]
					for day in range(1, total_days+1):
						filenames.append("%04d-%02d/%04d-%02d-%02d" % (start_year, month, start_year, month, day))
			elif start_year != end_year and year_loop == 1:
				for month in range(1, 13):
					total_days = monthrange(start_year, month)[1]
					for day in range(1, total_days+1):
						filenames.append("%04d-%02d/%04d-%02d-%02d" % (start_year, month, start_year, month, day))
			else:
				for month in range(1, end_month+1):
					total_days = monthrange(start_year, month)[1]
					for day in range(1, total_days+1):
						filenames.append("%04d-%02d/%04d-%02d-%02d" % (start_year, month, start_year, month, day))
			start_year += 1

	print("[%.4fs] Filenames generated. Start analyzing..." % elapsed())

	return filenames


def elapsed():
	""" Return elapsed time in seconds """
	return time.time()-START_TIME


def main():
	""" The program starts here. """

	start_time = time.time()

	# 2018 Update
	start_month = 3
	start_year = 2016
	end_month = 7
	end_year = 2018

	# Define an output queue
	output = mp.Queue()

	period = time_picker(start_month, start_year, end_month, end_year)

	print("[%.4fs] The program could take a several hours." % elapsed())

	if __name__ == '__main__':
		# Create a multiprocessing Pool
		pool = mp.Pool()
		pool.map(collector.analyze, period)

	print("[%.4fs] Analyzing complete. Zipping dictionaries..." % (elapsed()))

	dictionary.zipper(start_month, start_year, end_month, end_year)

	final_time = datetime.timedelta(seconds=elapsed())

	print("[%.4fs] ThaiTrend: Emoji has finished in %s " % (elapsed(), str(final_time)))
	print("Next: Run graph.py to visualize data into graphs.")

START_TIME = time.time()
print("============ ThaiTrend: Emoji (v1.1) is running... ============")
print()
print("================= Current machine information =================")
print('** Python version\t:', platform.python_version())
print('** Compiler\t\t:', platform.python_compiler())
print('** System\t\t:', platform.system(), platform.release())
print('** Processor\t\t:', platform.processor())
print('** CPU counts\t\t:', mp.cpu_count())
print('** Interpreter\t\t:', platform.architecture()[0])
print()

main()
