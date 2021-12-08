from darkimg.errors.unparsible import UnParsableError

class Create:
	img = None
	imgDidMount = False

	def __init__(self, data: str):
		if (type(data) != str):
			raise UnParsableError()
		self.img = data
		self.imgDidMount = True
	
	def didMount(self):
		return self.imgDidMount