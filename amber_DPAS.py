#!/usr/bin/env python3

import boonamber
import os
import sys
import csv
import numpy as np
from color_class import bcolors
from print_functions import print_summary
from print_functions import print_confusion_matrix as print_cm


class amber_DPAS:

	def __init__(self, args):

		self.user = args.user

		# check if given directory exists
		if not os.path.exists(args.directory):
			print('Directory must be an image or a directory of images. Path does not exist')
			os._exit(1)
		else:
			self.directory = args.directory

		self.sensor_id = args.sensorID
		self.threshold = args.threshold
		self.min_count = args.minCount

		self.fp = []
		self.tp = []
		self.fn = []
		self.tn = []

		self.amber = boonamber.AmberClient(license_file="~/.Amber.license", license_id=self.user)

	def process_directory(self):

		# loop through files in directory
		for file in os.listdir(self.directory):
			self.process_file(file)

		# print out summary
		print_summary(len(os.listdir(self.directory)), self.tp, self.fp, self.tn, self.fn)

		# print confusion matrix #
		if self.get_total_processed() != 0:
			print_cm(self.tp, self.fp, self.tn, self.fn)
		print()

	def process_file(self, file):
		print("\n***************************")
		print(f"{bcolors.HEADER}{file}{bcolors.ENDC}")

		# get data from file
		print("Loading data....", flush=True, end="\r")
		with open(os.path.join(self.directory, file), 'r') as f:
			csv_reader = csv.reader(f, delimiter=',')
			data = list(csv_reader)
			# drop header row
			data = data[1:]
			# drop first 6 columns: ship, engine, maintenance, closed/open, timestamp, part
			data = [[float(d) for d in row[6:]] for row in data]
			#18 column in end
		
		# check for minimum of minCount rows
		if len(data) < self.min_count:
			print("Too little data: {} rows".format(len(data)))
			return

		# stream data
		print("Streaming data....", flush=True, end="\r")
		try:
			results = self.amber.stream_sensor(self.sensor_id, data, save_image=False)
		except Exception as e:
			print(e)
			os._exit(1)
			return

		# average NI
		avg = round(np.mean(results['NI']), 2)
		print("average: {}       ".format(avg))

		# classify csv
		is_compliant = False if avg >= self.threshold else True
		if "Closed" in file and is_compliant:  # true negative
			print(f"{bcolors.OKGREEN}Closed{bcolors.ENDC}")
			self.tn.append(file)
		elif "Closed" in file and not is_compliant:  # false positive
			print(f"{bcolors.FAIL}FALSE POSITIVE{bcolors.ENDC}")
			self.fp.append(file)
		elif "Open" in file and is_compliant:  # false negative
			print(f"{bcolors.FAIL}FALSE NEGATIVE{bcolors.ENDC}")
			self.fn.append(file)
		else:  # true positive
			print(f"{bcolors.OKGREEN}Open{bcolors.ENDC}")
			self.tp.append(file)


	# get total number of files processed from the true/false positive/negative lists
	def get_total_processed(self):
		return len(self.fp) + len(self.tn) + len(self.tp) + len(self.fn)
