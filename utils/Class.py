
class OutMessage:

	@classmethod
	def success(cls, origin_file_path, new_file_path=None):
		out = f"Successful: File [{origin_file_path}] is updated."

		if new_file_path: 
			out += f"\nOld version of file is [{new_file_path}]"

		return out

	@classmethod
	def errorFile(cls):
		return "Error file: File not exist or is not python file"


