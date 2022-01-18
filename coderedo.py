#! /usr/bin/env python3

import os
from utils.functions import *
from utils.Class import *


def main():
	data = parser()
	
	file_path = data.file

	if not file_path:
		os.system(f"{__file__} --help")
		exit()
	elif not (os.path.exists(file_path) and isPythonFile(file_path)):
		print(OutMessage.errorFile())
		exit()

	file_content = getFileContent(file_path)
	new_file_path = None

	if data.get_old:
		# create old version version
		new_file_path = re.sub(r"(\.py)", r"-old.py", file_path)
		createNewFile(new_file_path, file_content)

	# reformating

	for i in range(len(file_content)):
		line = file_content[i]

		# replace start whitespaces by tabs
		file_content[i] = whitespacesToTabs(line)


	# update origin file
	updateFile(file_path, file_content)

	# success message
	print(OutMessage.success(file_path, new_file_path))

if __name__ == '__main__':
	main()