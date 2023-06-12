class ListNote:

	def __init__(self, console):
		self.console = console

	def execute(self):
		self.console.listNote()

	def __str__(self):
		return "Список заметок"
