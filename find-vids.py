import os

DIR = '/vids'


for f in os.listdir(DIR):
	if 'mp4' in f:
		print(f)

for f in os.listdir(DIR):
	if 'flv' in f.lower():
		print(f)


