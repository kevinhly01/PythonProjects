# Coded using PyQt5
# class vs module: Classes allow you to use millions of them, while module only one per program

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Main(QtWidgets.QMainWindow):

	def __init__(self):
			QtWidgets.QMainWindow.__init__(self)
			
			self.initUI()

	def initUI(self):
		closeAction = QtWidgets.QAction('Close',self)
		closeAction.setShortcut('Ctrl+Q')
		closeAction.setStatusTip('Close Notepad')
		closeAction.triggered.connect(self.close)

		newAction = QtWidgets.QAction('New', self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('Create New File')
		newAction.triggered.connect(self.newFile)


		saveAction = QtWidgets.QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save current file')
		saveAction.triggered.connect(self.saveFile)

		openAction = QtWidgets.QAction('Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open a file')
		openAction.triggered.connect(self.openFile)

		# add menubar to window
		menu = self.menuBar()
		fileMenu = menu.addMenu('File')
		fileMenu.addAction(closeAction)
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)

		# To write text
		self.text = QtWidgets.QTextEdit(self)
		self.setCentralWidget(self.text)


		self.setGeometry(100,100,1030,800)
		self.setWindowTitle("Kevin's Text Editor")
		self.show()

	def newFile(self):
		self.text.clear()

	def saveFile(self):
		#filename = QtWidgets.QFileDialog.getSaveFileName(self,'Save File', os.getenv('HOME'))
		filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))[0]
		f = open(filename, 'w')
		text = self.text.toPlainText()
		f.write(text)
		f.close()

	# PyQt5: getOpenFileName returns tuple
	def openFile(self):
		filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
		f = open(filename, 'r')
		filedata = f.read()
		self.text.setText(filedata)
		f.close()

def main():
	# Every PyQt5 application must create an application obj
	# sys.argv is a list in Python, which contains the 
	# command-line arguments passed to the script.
	app = QtWidgets.QApplication(sys.argv)

	# Instantiate/Create the Main Class to get an object
	main = Main()
	main.show()

	# Tell program to wait for us to close app before ending program
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()