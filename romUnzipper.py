#!Python 3

# Unzippter for extracting my large collection of roms

import os
import zipfile



folder_name = '/Users/yourfolderpath'
extension = '.zip'

os.chdir(folder_name)

for item in os.listdir(folder_name):
	if item.endswith(extension):
		file_name = os.path.abspath(item) # get full path of files
		zip_ref = zipfile.ZipFile(file_name)
		zip_ref.extractall(folder_name) # extract file to dir
		zip_ref.close() # close file
		os.remove(file_name) # delete zipped file