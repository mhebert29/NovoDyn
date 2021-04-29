#!/usr/bin/env python3
import sys
import os
import json

def findtags(folder,tag):
	for path in pathlib.Path.iterdir(folder):
		if path.is_file():
			with open(path) as f:
				data = json.load(f)
				for region in data[regions]:
					if tag in regions[tags]:
						return data[asset][name]
				
