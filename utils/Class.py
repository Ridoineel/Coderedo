
class OutMessage:

	@classmethod
	def success(cls, origin_file_path, new_file_path):
		return f"Successful: File [{origin_file_path}] is updated.\nOld version of file is [{new_file_path}]"

	@classmethod
	def errorFile(cls):
		return "Error file: File not exist or is not python file"


