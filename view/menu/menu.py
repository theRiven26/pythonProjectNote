

from view.menu.createNote import CreateNote
from view.menu.listNote import ListNote
from view.menu.openNote import OpenNote
from view.menu.deleteNote import DeleteNote
from view.menu.editNote import EditNote



class Menu:
	listMenu = []
	def __init__(self, console):
		self.console = console
		self.listMenu = [CreateNote(self.console),
		                 ListNote(self.console),
		                 OpenNote(self.console),
		                 EditNote(self.console),
		                 DeleteNote(self.console)]

	def printMenu(self):
		self.console.printMenu(self.listMenu)

	def execute(self, choice):
		self.listMenu[choice].execute()


