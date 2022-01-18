#! /usr/bin/env python3

import os
from utils.functions import *
from utils.Class import *


def main():
	
	file_path = getFilePath()

	if not file_path:
		os.system(f"{__file__} --help")
		exit()
	elif not (os.path.exists(file_path) and isPythonFile(file_path)):
		print(OutMessage.errorFile())
		exit()

	file_content = getFileContent(file_path)

	for i in range(len(file_content)):
		line = file_content[i]

		# replace start whitespaces by tabs
		file_content[i] = whitespacesToTabs(line)

	# create new file and put the update of file
	new_file_path = re.sub(r"(\.py)", r"-coderedo.py", file_path)

	createNewFile(new_file_path, file_content)

	# success message
	print(OutMessage.success(new_file_path))

if __name__ == '__main__':
	main()