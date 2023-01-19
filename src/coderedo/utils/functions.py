import argparse

def parser():
	parse = argparse.ArgumentParser()
	parse.add_argument("--path", "-p", help="python file (.py) or directory", type=str)
	parse.add_argument("--get-old", "-go", 
						help=" -go 1, to get old version of the files before reformating", 
						default=False, type=bool
					)
	parse.add_argument("--tab-size", "-t", help="python file path (.py)", type=int, default=4)

	return parse.parse_args()

def isPythonFile(file_path):
	return ".py" in file_path and file_path.index(".py") == len(file_path) - 3 # 3 for length of ".py"

def getFileContent(path: str) -> [str]:
	file = open(path, "r") 
	contents = file.readlines()

	return contents