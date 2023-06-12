import json
import os
from model.note import Note

class NotesManager:
	filePath = 'notes.json'
	notes = []

	def createNote(self, title, content):
	    self.notes.append(Note(title,content))
	    self.saveNotes()


	def saveNotes(self):
		with open(self.filePath, 'w') as file:
			json.dump([note.__dict__ for note in self.notes], file)


	def loadNotes(self):
		if os.path.exists(self.filePath):
			with open(self.filePath, 'r') as file:
				data = json.load(file)
				self.notes = [Note(**note) for note in data]


	def editNote(self, index, newTitle, newContent):
		note = self.getNote(index)
		note.title = newTitle
		note.content = newContent
		self.saveNotes()
		# self.notes[index].title = newTitle
		# self.notes[index].content = newContent


	def deleteNoteByIndex(self, index):
		del self.notes[index]

	def getListNotes(self):
		return self.notes

	def getNote(self,index):
		return self.notes[index]
