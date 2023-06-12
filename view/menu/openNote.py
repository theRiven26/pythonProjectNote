class OpenNote:

	def __init__(self, console):
		self.console = console

	def execute(self):
		self.console.openNote()

	def __str__(self):
		return "Открыть заметку"