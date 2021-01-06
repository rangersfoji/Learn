# pip install pyqt5

from PyQt5.QtWidgets import QMainWindow,QApplication # for window
import sys # run & exit application
from PyQt5 import QtGui # icon

class Window(QMainWindow):
	def __init__(self):
	 super().__init__()

	 self.title= "Lottery Report"
	 self.top = 100
	 self.left = 100
	 self.width = 1000
	 self.height = 500

	 self.InitWindow()

	def InitWindow(self):
		self.setWindowIcon(QtGui.QIcon("download.jfif"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)

		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())