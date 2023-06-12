class CreateNote:

	def __init__(self, console):
		self.console = console

	def execute(self):
		self.console.createNote()

	def __str__(self):
		return "Создать заметку"
