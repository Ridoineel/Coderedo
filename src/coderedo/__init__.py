import os
from glob import glob
import shutil
import re

try:
	from utils.functions import *
	from utils.Class import Color
except:
	from .utils.functions import *
	from .utils.Class import Color

class CodeRedo:
	def __init__(self, directory, tab_size=4, get_old=False):
		self.directory = directory
		self.tab_size = tab_size
		self.get_old = get_old
		self.files = self.getDirFiles(self.directory, pattern=r".*\.py$")
		self.transformers = self._setTransformer(self.files)

	def getDirFiles(self, path, pattern=None):
		paths = []

		if os.path.isfile(path):
			res = [path]

			if pattern and re.match(pattern, path) is None:
				res = []

			return res

		for path in glob(os.path.join(path, "*")):
			paths.extend(self.getDirFiles(path, pattern))

		return paths

	def _setTransformer(self, files):
		res = {}

		for path in files:
			coderedo = CodeRedoOneFile(path, self.tab_size, self.get_old)

			res[path] = coderedo

		return res

	def fit(self):
		# reformating

		for coderedo in self.transformers.values():
			coderedo.fit()

	def update(self):
		for coderedo in self.transformers.values():
			coderedo.update(get_old=False)

		if self.get_old:
			new_path = self.getOldVersion(self.directory)

			if new_path:
				print(OutMessage.successForOldVersion(self.directory,  new_path))

	def getOldVersion(self, path):
		if os.path.isfile(path):
			new_path = re.sub(r"(\.py)$", r"-old.py", path)

			shutil.copy(path, new_path)
		else:
			new_path = path + "-old"
			shutil.copytree(path, new_path)

		return new_path

	def createFile(self, path, content: [str]):
		# create file (@path) and
		# add each line of @content

		with open(path, "w") as file:
			for line in content:
				file.write(line)


class CodeRedoOneFile: # OneFile
	def __init__(self, file_path, tab_size=4, get_old=False):
		self.file_path = file_path
		self.tab_size = tab_size
		self.get_old = get_old
		self.content = [] # lines of the file
		self.content_transformed = [] # lines of the updated file 

	def fit(self):
		# reformating
		self.content = getFileContent(self.file_path)

		for i in range(len(self.content)):
			line = self.content[i]

			# replace start whitespaces by tabs
			# and add it to content_transformed
			self.content_transformed.append(self.whitespacesToTabs(line))

	def update(self, get_old=None):
		if get_old == None:
			get_old = self.get_old

		new_file_path = ""

		self.createFile(self.file_path, self.content_transformed)
		
		# success message
		print(OutMessage.successForUpdate(self.file_path))

		if get_old:
			self.getOldVersion(self.file_path) 
		
			# success message
			print(OutMessage.successForOldVersion(self.file_path, new_file_path))

	def getOldVersion(self, file_path):
		new_file_path = re.sub(r"(\.py)$", r"-old.py", file_path)

		self.createFile(new_file_path, self.content)

	def createFile(self, path, content: [str]):
		# create file (@path) and
		# add each line of @content

		with open(path, "w") as file:
			for line in content:
				file.write(line)


	def whitespacesToTabs(self, string):
		""" Replace all start whitespaces (with tab) to tabulations once 

		"""

		tab_size = self.tab_size
		spaces = 0
		tabs = 0

		# count first white space 
		# of the line
		for char in string:
			if char == " ":
				spaces += 1
			elif char == "\t":
				tabs += 1
			else:
				break

		tabs += round(spaces/tab_size)

		new_string = re.sub(r"^(( |\t)+)", "\t" * tabs, string)

		return new_string


class OutMessage:

	@classmethod
	def successForUpdate(cls, origin_file_path):
		_type = ["file", "directory"][os.path.isdir(origin_file_path)]

		message = f"[coderedo] Successful: The {_type} \"{origin_file_path}\" is updated."

		return Color.primary(message)

	@classmethod
	def successForOldVersion(cls, origin_file_path, new_file_path):
		_type = ["file", "directory"][os.path.isdir(origin_file_path)]

		message = f"\n[coderedo] The old version of the {_type} \"{origin_file_path}\" is \"{new_file_path}\""

		return Color.primary(message)
