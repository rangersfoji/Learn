from PyQt5.QtWidgets import QApplication ,QPushButton, QDialog  , QGroupBox,QHBoxLayout,QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):
	def __init__(self):
		super().__init__()


		self.title = 'diolog'
		self.left = 100
		self.top = 100
		self.width = 500
		self.height = 100

		self.ini_Window()
		

	def ini_Window(self):
		self.setWindowIcon(QtGui.QIcon('download.jfif'))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)

		self.createLayout()
		vbox = QVBoxLayout();
		vbox.addWidget(self.groupBox)
		self.setLayout(vbox)

		self.show()

	def createLayout(self):
		self.groupBox = QGroupBox('What Is yur favorite sport ? ')
		hboxLayout = QHBoxLayout()

		football_btn = self.createButton('Football',100,100,50,40)
		football_btn.setMinimumHeight(40)
		hboxLayout.addWidget(football_btn)

		cricket_btn = self.createButton('Cricket',100,100,50,40)
		cricket_btn.setMinimumHeight(40)
		hboxLayout.addWidget(cricket_btn)

		tennis_btn = self.createButton('Tennis',100,100,50,40)
		tennis_btn.setMinimumHeight(40)
		hboxLayout.addWidget(tennis_btn)

		self.groupBox.setLayout(hboxLayout)


	def createButton(self,name,left,top,width,height):
		button = QPushButton(name,self)
		button.setGeometry(QRect(left,top,width,height))
		return button


		# button = QPushButton('exit',self)
		# button.setGeometry(QRect(500,10,80,50))
		# button.setIcon(QtGui.QIcon('download.jfif'))
		# button.setIconSize(QtCore.QSize(40,40))
		# button.setToolTip('<h2>This will close the program</h2>') 
		# button.clicked.connect(self.clicked)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())
