#! /usr/bin/env python3

import os

try:
	from utils.functions import parser
	from utils.Class import Color
	from __init__ import CodeRedo
except Exception as e:
	from .utils.functions import parser
	from .utils.Class import Color
	from .__init__ import CodeRedo


def main():
	data = parser()
	
	path = data.path
	tab_size = data.tab_size
	get_old = data.get_old
	
	if not path:
		os.system(f"{__file__} --help")
		exit()
	elif not (os.path.exists(path)):
		print(Color.danger("[coderedo] Error: File or directory not exist"))
		exit()

	coderedo = CodeRedo(path, tab_size, get_old)

	# reformat files's text
	coderedo.fit()

	# update files
	coderedo.update()

if __name__ == '__main__':
	main()