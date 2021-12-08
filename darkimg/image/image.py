from darkimg.lexer.lexer import Lexer
from darkimg.builtins import builtin_colors
import sys

class Image:

	colors = []

	def __init__(self, data: Lexer):
		for color in data.lexed:
			self.colors.append(''.join(chr(i) for i in color))
		self.color2ascii() # Builtin colors to ascii

	def color2ascii(self):
		index = -1
		for color in self.colors:
			index += 1
			try:
				self.colors[index] = builtin_colors[color]
			except KeyError:
				pass
	
	def draw(self):
		index = 0
		for toDraw in self.colors:
			index += 1
			if (index == 63):
				sys.stdout.write(toDraw + " \033[m\n")
				index = 0
			else:
				sys.stdout.write(toDraw + " \033[m")
		print()
