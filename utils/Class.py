
class Color:
	success = lambda _str: '\033[92m' + _str + '\033[0m'
	danger = lambda _str: '\033[91m' + _str + '\033[0m'
	primary = lambda _str: '\033[96m' + _str + '\033[0m'
	warning = lambda _str: '\033[33m' + _str + '\033[0m'

class Style:
	bold = lambda _str: '\033[1m' + _str + '\033[0m'
	underline = lambda _str: '\033[4m' + _str + '\033[0m'
	blink = lambda _str: '\033[5m' + _str + '\033[0m'


class OutMessage:

	@classmethod
	def success(cls, origin_file_path, new_file_path=None):
		message = f"[coderedo] Successful: File [{origin_file_path}] is updated."

		if new_file_path: 
			message += f"\n[coderedo] Old version of file is [{new_file_path}]"

		return Color.primary(message)

	@classmethod
	def errorFile(cls):
		message = Color.danger("[coderedo] Error file: File not exist or is not python file")
		
		return message


