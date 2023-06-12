class EditNote:

	def __init__(self, console):
		self.console = console

	def execute(self):
		self.console.editNote()

	def __str__(self):
		return "Изменить заметку"
