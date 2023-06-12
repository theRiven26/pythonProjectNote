from view.menu.menu import Menu
from presenter.presenter import Presenter


title:str
content:str
date:str

class Console:
	presenter = Presenter()
	def __init__(self):
		self.menu = Menu(self)
		self.presenter = Presenter()

	def createNote(self):
		title = input("Заголовок: ")
		content = input("Содержимое записи: ")
		self.presenter.createNote(title, content)

	def listNote(self):
		listNote = self.presenter.listNote()
		for i, note in enumerate(listNote):
			print(f"{i + 1}. {note.title}")
		print("")

	def openNote(self):
		note = self.presenter.openNote(self.inputIndexNote())
		print(f"Заголовок: {note.title}")
		print(f"Содержание: {note.content}")
		print("")

	def deleteNote(self):
		self.presenter.deleteNote(self.inputIndexNote())

	def editNote(self):
		inputIndex = self.inputIndexNote()
		note = self.presenter.openNote(inputIndex)
		newTitle = input("Введите заголовок:")
		newContent = input("Введите заголовок:")
		self.presenter.editNote(inputIndex, newTitle, newContent)


	def printMenu(self, listMenu):
		for i, command in enumerate(listMenu):
			print(f" {i + 1}. {command}")

	def start(self):
		self.presenter.loadNotes()
		while True:
			self.menu.printMenu()
			try:
				choice = int(input(">>>: ",)) - 1
			except:
				print("Такого значения нет")
			if self.checkChoice(choice):
				self.menu.execute(choice)
			else:
				print("Такого действия нет")

	def checkChoice(self, choice):
		return choice < len(self.menu.listMenu)


	def inputIndexNote(self):
		listNote = self.presenter.listNote()
		index = int(input("Введите номер записи: ")) - 1
		if index < len(listNote):
			return index
		else:
			raise ValueError("Такой записи не существует")