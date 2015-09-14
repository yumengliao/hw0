#Yumeng Liao, yl2908, liquor counter

import csv

filename = 'iowa-liquor-sample.csv'
count = 0
search_for = 'single malt scotch'

with open(filename, 'rb') as liquor_file:
	read_file = csv.reader(liquor_file)
	for row in read_file:
		for entry in row:
			if entry.lower() == search_for:
				count = count + 1
				break

print count
