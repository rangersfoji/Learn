from PyQt5.QtWidgets import QApplication , QMainWindow,QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
import time
from PyQt5 import QtCore

start = time.time()


class Window(QMainWindow):
	def __init__ (self):
		super().__init__()

		self.title = 'push button'
		self.left = 100
		self.top = 100
		self.width = 1000
		self.height = 500

		self.ini_window()

	def ini_window(self):
		self.setWindowIcon(QtGui.QIcon('download.jfif'))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)

		self.Uicomponents()
		self.show()

	def Uicomponents(self):
		button = QPushButton('exit',self)
		button.setGeometry(QRect(500,10,80,50))
		button.setIcon(QtGui.QIcon('download.jfif'))
		button.setIconSize(QtCore.QSize(40,40))
		button.setToolTip('<h2>This will close the program</h2>') 
		button.clicked.connect(self.clicked)

	def clicked(self):
		print('close button clicked')
		sys.exit()





if __name__ == "__main__":  # use this because it is faster
	App = QApplication(sys.argv)
	window = Window()
	end = time.time()
	print(end - start)
	sys.exit(App.exec())

