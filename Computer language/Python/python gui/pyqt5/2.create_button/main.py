# for faster performance
# create and use method than simple because local variable is faster than gloabal variable
# use like below 'if __name == "__main__" after that 
# 				  main()  and in main() method write those code it's faster '
# use (string , list ...)comprihension
# use map, filter (that type of short line code) which are built in function and faster than normal fuction



from PyQt5.QtWidgets import QApplication , QMainWindow,QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
import time

start = time.time()


class Window(QMainWindow):
	def __init__ (self):
		super().__init__()

		title = 'push button'
		left = 100
		top = 100
		width = 1000
		height = 500
	
		self.setWindowIcon(QtGui.QIcon('download.jfif'))
		self.setWindowTitle(title)
		self.setGeometry(left,top,width,height)

		self.Uicomponents()
		self.show()

	def Uicomponents(self):
		button = QPushButton('Save',self)
		# button.move(50,50)
		button.setGeometry(QRect(500,10,100,30))


if __name__ == "__main__":  # use this because it is faster
	App = QApplication(sys.argv)
	window = Window()
	end = time.time()
	print(end - start)
	sys.exit(App.exec())

