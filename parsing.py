#!/usr/bin/env python3

import sys
import os
import json
import pathlib
from pathlib import Path


def findtags(folder,tags):
	outlist = {}
	filteredtags = {}
	for filename in os.listdir(folder):
		for tag in tags:
			filteredtags[tag] = False;
		mypath = folder + "/" + filename
		with open(mypath) as f:
			data = json.load(f)
			for region in data["regions"]:
				for intag in region["tags"]:
					if intag in filteredtags:
						filteredtags[intag] = True
		if all(filteredtags.values()):
			outlist[len(data["regions"])] = data["asset"]["name"]
	return outlist
			
if __name__ == "__main__":
	if len(sys.argv) < 3 or len(sys.argv) >3:
		print("Usage:    [program] [json directory] [list of tags to search for]")
		exit()
	findtags(sys.argv[1], sys.argv[2])
		
			
			
			
		
