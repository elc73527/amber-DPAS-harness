#!/usr/bin/env python3

import os
import sys
import argparse
from amber_DPAS import amber_DPAS


def main_help():
	help = '''\

	amber <command>

	options for processing data through amber
	'''

	print(help)

	print('\t--user (-u)\n\t\tREQUIRED\n\t\ttype : string\n\t\tdescription : user ID for the Boon Amber account')
	print('\t--directory (-d)\n\t\tREQUIRED\n\t\ttype : string\n\t\tdescription : path to image set or image from current directory')
	print('\t--sensorID (-s)\n\t\tREQUIRED\n\t\ttype : string\n\t\tdescription : Boon ID for model')
	print('\t--threshold (-t)\n\t\tREQUIRED\n\t\ttype : int\n\t\tdescription : threshold for the average NI to classify file')
	print('\t--minCount (-m)\n\t\tREQUIRED\n\t\ttype : int\n\t\tdescription : minimum number of rows required int eh dataset to process')

	print()
	os._exit(0)

def parse_arguments(argv):
	# arg parser to init
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--user', nargs='?', required=True, type=str,
						help="user ID for amber")
	parser.add_argument('-d', '--directory', nargs='?', required=True, type=str,
						help="file or directory to process")
	parser.add_argument('-s', '--sensorID', nargs='?', required=True, type=str,
						help="file or directory to process")
	parser.add_argument('-t', '--threshold', nargs='?', required=True, type=int,
						help="threshold for average NI per dataset")
	parser.add_argument('-m', '--minCount', nargs='?', required=True, type=int,
						help="minimum number of rows in order to process")
	args = parser.parse_args(argv)

	return args


def main(argv):

	if len(argv) == 0:
		main_help()

	args = parse_arguments(argv)

	amber_process = amber_DPAS(args)

	try:
		amber_process.process_directory()
	except KeyboardInterrupt:
		print('\nInterrupted')
		os._exit(1)


if __name__ == "__main__":
	main(sys.argv[1:])