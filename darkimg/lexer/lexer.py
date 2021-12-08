from darkimg.create.img import Create
from darkimg.errors.notanimage import NotAnImage
from darkimg.errors.invalidsyntax import InvalidSyntax

class Lexer:
	data: str = None

	lexed = []

	def __init__(self, img: Create):
		if (type(img) != Create):
			raise NotAnImage()
		self.data = img.img
	
	def lex(self):
		# Prepare string
		toLex = self.data.lstrip("\n").rstrip("\n")
		lines = toLex.split("\n")
		# Lex
		colors = []
		index = -1
		for line in lines:
			index += 1
			color = None
			try:
				color = line.split('[')[1].split(']')[0]
			except IndexError:
				raise InvalidSyntax()
			colors.append(list(color.encode('ascii')))
		self.lexed = colors

	def getLexed(self):
		return self.lexed