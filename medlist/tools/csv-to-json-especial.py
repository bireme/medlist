#!coding: utf-8
import csv
import json
import sys
import os
from glob import glob

dir = 'csv_dados/especial/new'
app = "medicine"

files = []
for file in glob(dir + "/*.*"):

	line_file = {}
	model = file.split("/")[-1].replace('.csv', '')
	
	line_file['model'] = model
	line_file['file'] = file

	if '\0' in open(file).read():
		content = open(file).read().replace('\0', '')
		open(file, 'w').write(content)

	files.append(line_file)

for file in files:

	if 'MedicineApp_Local_pipe' in file['file']:
		continue
	
	if 'MedicineRef_pipe.csv' in file['file']:
		continue

	if 'ModelFormularyInfo_Local_pipe' in file['file']:
		continue

	if '_pipe' in file['model']:
		file['model'] = file['model'].replace('_pipe', '')

	meta_file = file
	print '-> Converting %s..' % file['file']


	file = csv.reader(open(file['file'], 'rb'), delimiter='|')

	rownum = 0
	header = []
	data = []
	for row in file:

		if rownum == 0:
			for item in row:
				header.append(item.strip())
		else:
			new_row = []
			for item in row:
				new_row.append(item.strip())
			data.append(new_row)

		rownum += 1

	response = []
	for row in data:
		
		new_row = {}

		itemnum = 0
		for item in row:
			key = header[itemnum]
			
			new_row[key] = item
			itemnum += 1

		response.append(new_row)

	output = json.dumps(response, indent=2)
	open('json/%s.json' % meta_file['model'],'w').write(output)
			


		