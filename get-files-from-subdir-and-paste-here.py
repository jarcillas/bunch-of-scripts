## This script copies all files within each subdirectory and pastes them in the current directory. 

import os, path, shutil

currentdir = os.getcwd()
subdirs = [x[0] for x in os.walk(currentdir)]
print(subdirs)

for i in subdirs[1:]:
	files = os.listdir(i)
	for file_name in files:
		full_file_name = os.path.join(i, file_name)
		if os.path.isfile(full_file_name):
			shutil.copy(full_file_name, currentdir)