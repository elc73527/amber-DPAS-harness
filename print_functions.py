#!/usr/bin/env python3

from color_class import bcolors

def print_summary(total_files, tp, fp, tn, fn):
	# print out summary
	print("\nTotal compliant files: {}".format(len(fp) + len(tn)))
	print("Total defect files: {}".format(len(tp) + len(fn)))
	print("Number of excluded files (too few rows): {}".format(
		total_files - (len(fp) + len(tn) + len(tp) + len(fn))))

def print_confusion_matrix(tp, fp, tn, fn):
	total_count = len(fn) + len(tn) + len(fp) + len(tp)
	total_compliant = len(fp) + len(tn)
	total_defect = len(tp) + len(fn)

	print("-----------------------------------------------")
	print(f"|//////////////| {bcolors.BOLD}Boon Compliant{bcolors.ENDC} | {bcolors.BOLD}Boon Defect{bcolors.ENDC} |")
	print("-----------------------------------------------")

	print(f"| {bcolors.BOLD}GT Compliant{bcolors.ENDC} |", flush=True, end="")
	print(f"{bcolors.OKGREEN}{str(int(len(tn) / total_compliant * 100)) + '%':^16}{bcolors.ENDC}", flush=True, end="")
	print(f"|", flush=True, end="")
	print(f"{bcolors.FAIL}{str(int(len(fp) / total_compliant * 100)) + '%':^13}{bcolors.ENDC}", flush=True, end="")
	print("|")

	print(f"|  {bcolors.BOLD}GT Defect{bcolors.ENDC}   |", flush=True, end="")
	print(f"{bcolors.FAIL}{str(int(len(fn) / total_defect * 100)) + '%':^16}{bcolors.ENDC}", flush=True, end="")
	print("|", flush=True, end="")
	print(f"{bcolors.OKGREEN}{str(int(len(tp) / total_defect * 100)) + '%':^13}{bcolors.ENDC}", flush=True, end="")
	print(f"|")
	print("-----------------------------------------------")