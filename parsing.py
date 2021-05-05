#!/usr/bin/env python3
import sys
import os
import json
import pathlib
from pathlib import Path
def findtags(folder,tag):
	for filename in os.listdir(folder):
		mypath = folder + "/" + filename
		with open(mypath) as f:
			data = json.load(f)
			for region in data["regions"]:
				if tag in region["tags"]:
					return data["asset"]["path"]
			
if __name__ == "__main__":
	istherepath = False
	for arg in sys.argv[1:]:
		if not istherepath:
			path = arg
			istherepath = True
		else:
			tag = arg
			print(findtags(path, tag))
			istherepath = False
			
			
			
		
