# Coded using PyQt5
# class vs module: Classes allow you to use millions of them, while module only one per program

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtCore import Qt

class Main(QtWidgets.QMainWindow):

	# Note: needed parent for new file to work
	def __init__(self, parent = None):
			QtWidgets.QMainWindow.__init__(self,parent)
			self.filename = ""
			self.changesSaved = True
			self.initUI()

	def initFeatures(self):
		self.closeAction = QtWidgets.QAction(QtGui.QIcon("icons/close.png"), 'Close',self)
		self.closeAction.setShortcut('Ctrl+Q')
		self.closeAction.setStatusTip('Close Notepad')
		self.closeAction.triggered.connect(self.close)

		self.newAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"), 'New', self)
		self.newAction.setShortcut('Ctrl+N')
		self.newAction.setStatusTip('Create New File')
		self.newAction.triggered.connect(self.newFile)

		self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"), 'Open', self)
		self.openAction.setShortcut('Ctrl+O')
		self.openAction.setStatusTip('Open a file')
		self.openAction.triggered.connect(self.openFile)

		self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/save.png"), 'Save', self)
		self.saveAction.setShortcut('Ctrl+S')
		self.saveAction.setStatusTip('Save current file')
		self.saveAction.triggered.connect(self.saveFile)

		self.printAction = QtWidgets.QAction(QtGui.QIcon("icons/print.png"), 'Print Document', self)
		self.printAction.setShortcut('Ctrl+P')
		self.printAction.setStatusTip('Print document')
		self.printAction.triggered.connect(self.printFile)

		self.previewAction = QtWidgets.QAction(QtGui.QIcon("icons/preview.png"), "Preview Document", self)
		self.previewAction.setShortcut('Ctrl+Shift+P')
		self.previewAction.setStatusTip('Preview Document')
		self.previewAction.triggered.connect(self.previewFile)

		self.cutAction = QtWidgets.QAction(QtGui.QIcon("icons/cut.png"), "Cut", self)
		self.cutAction.setShortcut('Ctrl+C')
		self.cutAction.setStatusTip('Delete text')
		self.cutAction.triggered.connect(self.text.cut)

		self.copyAction = QtWidgets.QAction(QtGui.QIcon("icons/copy.png"), "Copy", self)
		self.copyAction.setShortcut('Ctrl+X')
		self.copyAction.setStatusTip('Copy text to clipboard')
		self.copyAction.triggered.connect(self.text.copy)

		self.pasteAction = QtWidgets.QAction(QtGui.QIcon("icons/paste.png"), "Paste", self)
		self.pasteAction.setShortcut('Ctrl+V')
		self.pasteAction.setStatusTip('Paste text from clipboard')
		self.pasteAction.triggered.connect(self.text.paste)

		self.undoAction = QtWidgets.QAction(QtGui.QIcon("icons/undo.png"), "Undo", self)
		self.undoAction.setShortcut('Ctrl+Z')
		self.undoAction.setStatusTip('Undo Previous Action')
		self.undoAction.triggered.connect(self.text.undo)

		self.redoAction = QtWidgets.QAction(QtGui.QIcon("icons/redo.png"), "Redo", self)
		self.redoAction.setShortcut('Ctrl+Y')
		self.redoAction.setStatusTip('Redo last action that was undone')
		self.redoAction.triggered.connect(self.text.redo)

		self.bulletAction = QtWidgets.QAction(QtGui.QIcon("icons/bullet.png"), "Insert bullet List", self)
		self.bulletAction.setShortcut('Ctrl+Shift+B')
		self.bulletAction.setStatusTip('Insert bulleted list')
		self.bulletAction.triggered.connect(self.bulletList)

		self.numberedAction = QtWidgets.QAction(QtGui.QIcon("icons/number.png"), "Insert numbered List", self)
		self.numberedAction.setShortcut('Ctrl+Shift+L')
		self.numberedAction.setStatusTip('Insert numbered list')
		self.numberedAction.triggered.connect(self.numList)

	def initMenu(self):
		# MENU
		menu = self.menuBar()
		fileMenu = menu.addMenu('File')
		editMenu = menu.addMenu('Edit')
		viewMenu = menu.addMenu('View')


		fileMenu.addAction(self.closeAction)
		fileMenu.addAction(self.newAction)
		fileMenu.addAction(self.openAction)
		fileMenu.addAction(self.saveAction)
		fileMenu.addAction(self.previewAction)
		fileMenu.addAction(self.printAction)

		editMenu.addAction(self.cutAction)
		editMenu.addAction(self.copyAction)
		editMenu.addAction(self.pasteAction)
		editMenu.addAction(self.undoAction)
		editMenu.addAction(self.redoAction)

		toolbarAction = QtWidgets.QAction("Toggle Toolbar", self)
		toolbarAction.triggered.connect(self.toggleToolbar)

		formatbarAction = QtWidgets.QAction("Toggle Formatbar", self)
		formatbarAction.triggered.connect(self.toggleFormatbar)

		statusbarAction = QtWidgets.QAction("Toggle Statusbar", self)
		statusbarAction.triggered.connect(self.toggleStatusbar)

		viewMenu.addAction(toolbarAction)
		viewMenu.addAction(formatbarAction)
		viewMenu.addAction(statusbarAction)

	def initToolbar(self):

		# TOOLBAR
		self.toolbar = self.addToolBar("Options")
		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)

		self.toolbar.addSeparator()

		self.toolbar.addAction(self.previewAction)
		self.toolbar.addAction(self.printAction)

		self.toolbar.addSeparator()

		self.toolbar.addAction(self.cutAction)
		self.toolbar.addAction(self.copyAction)
		self.toolbar.addAction(self.pasteAction)
		self.toolbar.addAction(self.undoAction)
		self.toolbar.addAction(self.redoAction)

		self.toolbar.addSeparator()

		self.toolbar.addAction(self.bulletAction)
		self.toolbar.addAction(self.numberedAction)

		self.addToolBarBreak()

	def initFormatbar(self):
		fontBox = QtWidgets.QFontComboBox(self)
		fontBox.currentFontChanged.connect(self.currFont)

		fontSize = QtWidgets.QComboBox(self)
		fontSize.setEditable(True)

		fontSize.setMinimumContentsLength(3)

		fontSize.activated.connect(self.fontSize)

		fontSizes = ['6','7','8','9','10','11','12','13',
					 '14','15','16','18','20','22','24',
		             '26','28','32','36','40','44','48',
		             '54','60','66','72','80','88','96']
		for i in fontSizes:
			fontSize.addItem(i)

		fontColor = QtWidgets.QAction(QtGui.QIcon("icons/font-color.png"), "Change Font Color", self)
		fontColor.triggered.connect(self.fontColor)

		backColor = QtWidgets.QAction(QtGui.QIcon("icons/highlight.png"), "Change background Color", self)
		backColor.triggered.connect(self.highlight)

		boldAction = QtWidgets.QAction(QtGui.QIcon("icons/bold.png"), "Bold", self)
		boldAction.triggered.connect(self.bold)

		italicAction = QtWidgets.QAction(QtGui.QIcon("icons/italic.png"), "Italicize", self)
		italicAction.triggered.connect(self.italic)

		underlineAction = QtWidgets.QAction(QtGui.QIcon("icons/underline.png"), "Underline", self)
		underlineAction.triggered.connect(self.underline)

		strikeAction = QtWidgets.QAction(QtGui.QIcon("icons/strike.png"), "Strike", self)
		strikeAction.triggered.connect(self.strike)
		
		superAction = QtWidgets.QAction(QtGui.QIcon("icons/superscript.png"), "Superscript", self)
		superAction.triggered.connect(self.superScript)
		
		subscriptAction = QtWidgets.QAction(QtGui.QIcon("icons/subscript.png"), "Subscript", self)
		subscriptAction.triggered.connect(self.subScript)

		alignLeft = QtWidgets.QAction(QtGui.QIcon("icons/align-left.png"), "Align Left", self)
		alignLeft.triggered.connect(self.alignLeft)

		alignCenter = QtWidgets.QAction(QtGui.QIcon("icons/align-center.png"), "Algin Center", self)
		alignCenter.triggered.connect(self.alignCenter)

		alignRight = QtWidgets.QAction(QtGui.QIcon("icons/align-right.png"), "Algin Right", self)
		alignRight.triggered.connect(self.alignRight)

		alignJustify = QtWidgets.QAction(QtGui.QIcon("icons/align-justify.png"), "Algin Justify", self)
		alignJustify.triggered.connect(self.alignJustify)

		self.formatbar= self.addToolBar("Format")

		self.formatbar.addWidget(fontBox)
		self.formatbar.addWidget(fontSize)

		self.formatbar.addSeparator()

		self.formatbar.addAction(fontColor)
		self.formatbar.addAction(backColor)

		self.formatbar.addSeparator()

		self.formatbar.addAction(boldAction)
		self.formatbar.addAction(italicAction)
		self.formatbar.addAction(underlineAction)
		self.formatbar.addAction(strikeAction)
		self.formatbar.addAction(superAction)
		self.formatbar.addAction(subscriptAction)

		self.formatbar.addSeparator()

		self.formatbar.addAction(alignLeft)
		self.formatbar.addAction(alignCenter)
		self.formatbar.addAction(alignRight)
		self.formatbar.addAction(alignJustify)

	def initUI(self):
		# To write text
		self.text = QtWidgets.QTextEdit(self)
		self.setCentralWidget(self.text)

		self.initFeatures()
		self.initMenu()
		self.initToolbar()
		self.initFormatbar()

		self.statusbar = self.statusBar()

		self.text.cursorPositionChanged.connect(self.cursorPosition)
		self.text.textChanged.connect(self.changed)

		self.setGeometry(300,300,1030,800)
		self.setWindowTitle("Kevin's Text Editor")
		self.setWindowIcon(QtGui.QIcon("icons/icon.png"))
		self.text.setTabStopWidth(33)

		self.show()

	def newFile(self):
		new_file = Main(self)
		new_file.show()

	def saveFile(self):
		if not self.filename:
			self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))[0]

		if not self.filename.endswith(".writer"):
			self.filename += ".writer"

		with open(self.filename,"wt") as file:
			file.write(self.text.toHtml())

	# PyQt5: getOpenFileName returns tuple
	def openFile(self):
		self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))[0]

		if self.filename:
			with open(self.filename,"rt") as file:
				self.text.setText(file.read())

	def printFile(self):
		printDialog = QtPrintSupport.QPrintDialog()

		if printDialog.exec() == QtWidgets.QDialog.Accepted:
			self.text.document().print_(dialog.printer())

	def previewFile(self):
		preview = QtPrintSupport.QPrintPreviewDialog()
		preview.paintRequested.connect(self.text.print_)
		preview.exec()

	def bulletList(self):
		#cursor = QtGui.QTextCursor(self).QTextCursor()
		cursor = self.text.textCursor()
		cursor.insertList(QtGui.QTextListFormat.ListDisc)

	def numList(self):
		cursor = self.text.textCursor()
		cursor.insertList(QtGui.QTextListFormat.ListDecimal)

	def cursorPosition(self):
		cursor = self.text.textCursor()

		line = cursor.blockNumber() + 1
		col = cursor.columnNumber() + 1

		self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

	def changed(self):
		self.changesSaved= False

	def closeEvent(self,event):
		if self.changesSaved:
			event.accept()
		else:
			msgBox= QtWidgets.QMessageBox(self)
			msgBox.setIcon(QtWidgets.QMessageBox.Warning)
			msgBox.setText("The document has been modified")
			msgBox.setInformativeText("Do you want to save your changes?")
			msgBox.setStandardButtons(QtWidgets.QMessageBox.Save   |
									 QtWidgets.QMessageBox.Cancel |
									 QtWidgets.QMessageBox.Discard)
			msgBox.setDefaultButton(QtWidgets.QMessageBox.Save)

			answer = msgBox.exec()

			if answer == QtWidgets.QMessageBox.Save:
				self.save()

			elif answer == QtWidgets.QMessageBox.Discard:
				event.accept()

			else:
				event.ignore()

	def currFont(self,font):
		self.text.setCurrentFont(font)

	def fontSize(self,fontsize):
		self.text.setFontPointSize(int(fontsize))

	def fontColor(self):

		color = QtWidgets.QColorDialog.getColor()

		self.text.setTextColor(color)

	def highlight(self):
		color = QtWidgets.QColorDialog.getColor()
		self.text.setTextBackgroundColor(color)

	def bold(self):
		if self.text.fontWeight() == 50:
			self.text.setFontWeight(int(75))
		else:
			self.text.setFontWeight(int(50))

	def italic(self):
		if not self.text.fontItalic():
			self.text.setFontItalic(True)
		else:
			self.text.setFontItalic(False)

	def underline(self):
		if not self.text.fontUnderline():
			self.text.setFontUnderline(True)
		else:
			self.text.setFontUnderline(False)

	def strike(self):
		txt_fmt = self.text.currentCharFormat()

		if not txt_fmt.fontStrikeOut():
			txt_fmt.setFontStrikeOut(True)
		else:
			txt_fmt.setFontStrikeOut(False)

		self.text.setCurrentCharFormat(txt_fmt)

	def superScript(self):
		txt_fmt = self.text.currentCharFormat()
		vert_align = txt_fmt.verticalAlignment()

		if vert_align == QtGui.QTextCharFormat.AlignNormal:
			txt_fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
		else:
			txt_fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
		self.text.setCurrentCharFormat(txt_fmt)

	def subScript(self):
		txt_fmt = self.text.currentCharFormat()
		vert_align = txt_fmt.verticalAlignment()

		if vert_align == QtGui.QTextCharFormat.AlignNormal:
			txt_fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
		else:
			txt_fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
		self.text.setCurrentCharFormat(txt_fmt)

	def alignLeft(self):
		self.text.setAlignment(Qt.AlignLeft)

	def alignCenter(self):
		self.text.setAlignment(Qt.AlignCenter)

	def alignRight(self):
		self.text.setAlignment(Qt.AlignRight)

	def alignJustify(self):
		self.text.setAlignment(Qt.AlignJustify)

	def toggleToolbar(self):
		state = self.toolbar.isVisible()
		self.toolbar.setVisible(not state)

	def toggleFormatbar(self):
		state = self.formatbar.isVisible()
		self.formatbar.setVisible(not state)

	def toggleStatusbar(self):
		state = self.statusbar.isVisible()
		self.statusbar.setVisible(not state)


def main():
	# Every PyQt5 application must create an application obj
	# sys.argv is a list in Python, which contains the 
	# command-line arguments passed to the script.
	app = QtWidgets.QApplication(sys.argv)

	# Instantiate/Create the Main Class to get an object
	main = Main()
	main.show()

	# Tell program to wait for us to close app before ending program
	sys.exit(app.exec())

if __name__ == "__main__":
	main()