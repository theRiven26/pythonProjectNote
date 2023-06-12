
from model.notesManager import NotesManager

class Presenter:
	notesManager = NotesManager()

	def createNote(self, title, content):
		self.notesManager.createNote(title,content)

	def listNote(self):
		return self.notesManager.getListNotes()

	def openNote(self, index):
		return self.notesManager.getNote(index)

	def deleteNote(self, index):
		self.notesManager.deleteNoteByIndex(index)

	def loadNotes(self):
		self.notesManager.loadNotes()

	def editNote(self, index, newTitle, newContent):
		self.notesManager.editNote(index, newTitle, newContent)




