class DeleteNote:

	def __init__(self, console):
		self.console = console

	def execute(self):
		self.console.deleteNote()

	def __str__(self):
		return "Удалить заметку"
