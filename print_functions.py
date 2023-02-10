#!/usr/bin/env python3

import math
from color_class import bcolors

def print_summary(total_files, tp, fp, tn, fn):
	# print out summary
	print("\nTotal compliant files: {}".format(len(fp) + len(tn)))
	print("Total defect files: {}".format(len(tp) + len(fn)))
	print("Number of excluded files (too few rows): {}".format(
		total_files - (len(fp) + len(tn) + len(tp) + len(fn))))

def print_confusion_matrix(tp, fp, tn, fn):
	total_count = len(fn) + len(tn) + len(fp) + len(tp)
	total_compliant = len(fp) + len(tn) if len(fp) + len(tn) != 0 else 1
	total_defect = len(tp) + len(fn) if len(tp) + len(fn) != 0 else 1

	print("-----------------------------------------------")
	print(f"|//////////////| {bcolors.BOLD}Boon Compliant{bcolors.ENDC} | {bcolors.BOLD}Boon Defect{bcolors.ENDC} |")
	print("-----------------------------------------------")

	print(f"| {bcolors.BOLD}GT Compliant{bcolors.ENDC} |", flush=True, end="")
	print(f"{bcolors.OKGREEN}{str(int(math.ceil(len(tn) / total_compliant * 100))) + '%':^16}{bcolors.ENDC}", flush=True, end="")
	print(f"|", flush=True, end="")
	print(f"{bcolors.FAIL}{str(int(math.ceil(len(fp) / total_compliant * 100))) + '%':^13}{bcolors.ENDC}", flush=True, end="")
	print("|")

	print(f"|  {bcolors.BOLD}GT Defect{bcolors.ENDC}   |", flush=True, end="")
	print(f"{bcolors.FAIL}{str(int(math.ceil(len(fn) / total_defect * 100))) + '%':^16}{bcolors.ENDC}", flush=True, end="")
	print("|", flush=True, end="")
	print(f"{bcolors.OKGREEN}{str(int(math.ceil(len(tp) / total_defect * 100))) + '%':^13}{bcolors.ENDC}", flush=True, end="")
	print(f"|")
	print("-----------------------------------------------")