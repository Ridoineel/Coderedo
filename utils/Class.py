
class OutMessage:

	@classmethod
	def success(cls, path):
		return f"Successful: See change in new file [{path}]"

	@classmethod
	def errorFile(cls):
		return "Error file: File not exist or is not python file"


